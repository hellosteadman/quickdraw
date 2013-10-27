from django.conf import settings
from django.db.models import Count
from django.utils.html import escape
from quickdraw.qanda.models import Vote
from socketIO_client import SocketIO

def new_answer(answer):
	with SocketIO('localhost', settings.SOCKETIO_PORT) as socket:
		socket.emit('answerSent',
			{
				'answer': escape(answer.title),
				'question': answer.question.pk
			}
		)

def new_vote(answer):
	total_votes = Vote.objects.filter(answer__question = answer.question).count()
	results = []
	
	for result in answer.question.answers.annotate(vote_count = Count('votes')):
		results.append(
			{
				'answer': result.pk,
				'votes': result.vote_count,
				'percent': total_votes > 0 and (
					float(result.vote_count) / float(total_votes) * 100.0
				) or 0
			}
		)
	
	with SocketIO('localhost', settings.SOCKETIO_PORT) as socket:
		socket.emit('voteSent',
			{
				'answer': answer.pk,
				'question': answer.question.pk,
				'results': results
			}
		)