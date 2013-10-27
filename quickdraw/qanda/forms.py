from django import forms
from django.utils.timezone import now
from quickdraw.qanda.models import Question
from datetime import timedelta

class QuestionForm(forms.ModelForm):
	title = forms.CharField(
		max_length = 117,
		widget = forms.TextInput(
			attrs = {
				'placeholder': 'Give your question a title',
				'class': 'input-xlarge title'
			}
		)
	)
	
	kind = forms.CharField(
		widget = forms.HiddenInput
	)
	
	duration = forms.IntegerField(
		widget = forms.RadioSelect(
			choices = (
				(90, u'90'),
				(120, u'120'),
				(180, u'180'),
				(240, u'240'),
				(300, u'300')
			),
			attrs = {
				'class': 'duration'
			}
		)
	)
	
	def save(self, commit = True):
		question = super(QuestionForm, self).save(commit = False)
		question.opens = now()
		question.closes = question.opens + timedelta(seconds = self.cleaned_data['duration'])
		
		if commit:
			question.save()
		
		return question
	
	class Meta:
		model = Question
		fields = ('title', 'kind', 'public')