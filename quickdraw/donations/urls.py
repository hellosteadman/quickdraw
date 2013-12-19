from django.conf.urls import patterns, url
from bambu.bootstrap.decorators import body_classes
from quickdraw.donations.views import *

urlpatterns = patterns('',
	url(r'^$', donate, name = 'donate'),
	url(r'^thanks/$', body_classes(thanks, 'donations', 'donations-thanks'), name = 'donated_thanks')
)