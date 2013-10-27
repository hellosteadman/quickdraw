from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.utils.timezone import now
from django.db.models import Count
from django.contrib import messages
from quickdraw.qanda.models import Question, Answer, Vote
from quickdraw.qanda.forms import QuestionForm
from django.views.decorators.cache import never_cache
import random

@never_cache
def create(request):
	form = QuestionForm(request.POST or None)
	
	if request.user.is_authenticated() and request.method == 'POST' and form.is_valid():
		question = form.save(commit = False)
		question.creator = request.user
		question.save()
		
		for answer in request.POST.getlist('answer[]', []):
			if answer and answer.strip():
				question.answers.create(
					title = answer,
					creator = request.user
				)
		
		return HttpResponseRedirect(
			question.get_absolute_url()
		)
	
	return TemplateResponse(
		request,
		'home.html',
		{
			'form': form
		}
	)

@never_cache
def question(request, slug):
	question = get_object_or_404(Question, slug = slug)
	right_now = now()
	total_votes = Vote.objects.filter(answer__question = question).count()
	
	vote_cast = request.user.is_authenticated() and request.user.votes.filter(
		answer__question = question
	).exists() or False
	
	if request.method == 'POST':
		if question.closes <= right_now:
			if question.kind == 'p':
				messages.error(request, u'Sorry! Your vote wasn\'t submitted in time.')
			else:
				messages.error(request, u'Sorry! Your answers weren\'t submitted in time.')
		else:
			if question.kind == 'p':
				if vote_cast:
					messages.error(request, u'Sorry, but you can\'t vote more than once.')
				else:
					try:
						answer = question.answers.get(pk = request.POST.get('answer'))
					except Answer.DoesNotExist:
						messages.error(request, u'Sorry, that answer couldn\'t be found')
					except:
						messages.error(request, u'Sorry, but your vote couldn\'t be cast')
					else:
						answer.votes.create(
							voter = request.user
						)
				
						messages.success(request, u'Thanks for your vote!')
						return HttpResponseRedirect(
							question.get_absolute_url()
						)
			else:
				added = 0
				for answer in request.POST.getlist('answer[]'):
					if not answer and not title.trim():
						continue
					
					try:
						answer = question.answers.get(
							title__iexact = answer
						)
					except Answer.DoesNotExist:
						answer = question.answers.create(
							title = answer,
							creator = request.user
						)
						
						added += 1
					
					if not answer.votes.filter(voter = request.user).exists():
						answer.votes.create(voter = request.user)
				
				if added > 0:
					messages.success(request,
						u'Thanks for your answer%s. You can keep submitting them until the list closes.' % (
							added != 1 and 's' or ''
						)
					)
				
				return HttpResponseRedirect(question.get_absolute_url())
	
	results = []
	if question.closes > right_now:
		seconds = (question.closes - right_now).seconds
	else:
		seconds = 0
		r = lambda: random.randint(0,255)
		
		for result in question.answers.annotate(vote_count = Count('votes')).order_by('created'):
			results.append(
				{
					'title': result.title,
					'votes': result.vote_count,
					'percent': total_votes > 0 and (
						float(result.vote_count) / float(total_votes) * 100.0
					) or 0,
					'colour': '#%02X%02X%02X' % (r(), r(), r())
				}
			)
	
	kind = (question.kind == 'p' and 'poll' or 'list')
	auth = request.user.is_authenticated() and 'auth' or 'anon'
	state = seconds and 'open' or 'closed'
	
	return TemplateResponse(
		request,
		(
			'qanda/%s-%s-%s.html' % (kind, auth, state),
			'qanda/%s-%s.html' % (kind, auth),
			'qanda/%s-%s.html' % (kind, state),
			'qanda/%s.html' % kind,
			'qanda/question.html'
		),
		{
			'question': question,
			'answers': question.answers.order_by('created'),
			'remaining_seconds': seconds,
			'results': results,
			'vote_cast': vote_cast,
			'total_votes': total_votes,
			'title_parts': (question.title,)
		}
	)