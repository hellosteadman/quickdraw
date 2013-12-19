from django.conf.urls import patterns, include, url
from django.views.decorators.cache import never_cache
from django.contrib import admin
from bambu.bootstrap.views import DirectTemplateView
from bambu.bootstrap.decorators import body_classes
from quickdraw.qanda.forms import QuestionForm
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$',
		never_cache(
			body_classes(
				DirectTemplateView.as_view(
					template_name = 'home.html',
					extra_context = {
						'menu_selection': 'home',
						'title_parts': ('Create short-run polls and lists',),
						'form': QuestionForm()
					}
				), 'home'
			)
		),
		name = 'home'
	),
	url(r'^logout/$', 'quickdraw.views.logout', name = 'logout'),
	url(r'^', include('quickdraw.qanda.urls')),
	url(r'^donate/', include('quickdraw.donations.urls')),
	url(r'', include('social_auth.urls'))
)