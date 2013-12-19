from django.conf.urls import patterns, url
from bambu.bootstrap.decorators import body_classes
from quickdraw.qanda.views import create, question

urlpatterns = patterns('',
	url(r'create/', body_classes(create, 'qanda', 'create'), name = 'create_question'),
	url(r'(?P<slug>[\w]{7})/$', body_classes(question, 'qanda', 'question'), name = 'question')
)