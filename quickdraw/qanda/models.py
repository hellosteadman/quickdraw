from django.db import models
from datetime import timedelta
import random, string

class Question(models.Model):
	creator = models.ForeignKey('auth.User', related_name = 'created_questions')
	slug = models.SlugField(max_length = 7, unique = True)
	kind = models.CharField(max_length = 1, default = 'p',
		choices = (
			('p', u'poll'),
			('l', u'list')
		)
	)
	
	opens = models.DateTimeField(auto_now_add = True)
	closes = models.DateTimeField(editable = False)
	title = models.CharField(max_length = 117)
	public = models.BooleanField(default = True)
	tweeted = models.BooleanField(default = False)
	
	@models.permalink
	def get_absolute_url(self):
		return ('question', [self.slug])
	
	def __unicode__(self):
		return self.title
	
	def save(self, *args, **kwargs):
		if not self.slug:
			while True:
				self.slug = ''.join(random.sample(string.letters + string.digits, 7))
				if not Question.objects.filter(slug = self.slug).exists():
					break
		
		super(Question, self).save(*args, **kwargs)
	
	class Meta:
		get_latest_by = 'opens'
		ordering = ('-opens',)

class Answer(models.Model):
	question = models.ForeignKey(Question, related_name = 'answers')
	creator = models.ForeignKey('auth.User', related_name = 'created_answers')
	title = models.CharField(max_length = 255)
	created = models.DateTimeField(auto_now_add = True)
	
	def __unicode__(self):
		return self.title
	
	class Meta:
		get_latest_by = 'created'
		ordering = ('-created',)

class Vote(models.Model):
	answer = models.ForeignKey(Answer, related_name = 'votes')
	voter = models.ForeignKey('auth.User', related_name = 'votes')
	cast = models.DateTimeField(auto_now_add = True)
	
	class Meta:
		get_latest_by = 'cast'
		ordering = ('-cast',)