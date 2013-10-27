from django.contrib import admin
from quickdraw.qanda.models import Question

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('title', 'creator', 'kind', 'closes')
admin.site.register(Question, QuestionAdmin)