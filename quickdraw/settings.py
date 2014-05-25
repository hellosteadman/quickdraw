from settings_local import *
from os import path

TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('Steadman', 'mark@steadman.io'),
)

MANAGERS = ADMINS
TIME_ZONE = None
LANGUAGE_CODE = 'en-gb'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_DIRS = (
	path.join(path.dirname(__file__), 'static'),
)

BOWER_COMPONENTS_ROOT = path.abspath(path.dirname(__file__) + '/../')

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'djangobower.finders.BowerFinder'
)

SECRET_KEY = 'd\6Bh>Dnq2igYT%J4y#wM:<UtQRz,-jC1S};&.^X|/Ixo[v]L0$e+u5H9`b(pc'

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'bambu_analytics.middleware.AnalyticsMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'django.core.context_processors.request',
	'django.contrib.messages.context_processors.messages',
	'django.core.context_processors.tz',
	'bambu_bootstrap.context_processors.basics',
	'quickdraw.context_processors.settings'
)

ROOT_URLCONF = 'quickdraw.urls'
WSGI_APPLICATION = 'quickdraw.wsgi.application'
TEMPLATE_DIRS = (
	path.abspath(path.dirname(__file__) + '/../templates/'),
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.admin',
	'django.contrib.admindocs',
	'django.contrib.humanize',
	'raven.contrib.django.raven_compat',
	'south',
	'social_auth',
	'djangobower',
	'bambu_bootstrap',
	'bambu_cron',
	'bambu_analytics',
	'quickdraw.qanda',
	'quickdraw.donations'
)

BOWER_INSTALLED_APPS = (
	'bootstrap',
	'fontawesome'
)

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse'
		}
	},
	'loggers': {
		'django.request': {
			'level': 'ERROR',
			'propagate': True
		}
	}
}

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	'social_auth.backends.twitter.TwitterBackend',
)

LOGIN_REDIRECT_URL = '/'
SHORTURL_PROVIDER = 'bambu_urlshortener.providers.bitly.BitlyProvider'

BOOTSTRAP_NAVBAR_INVERSE = True
SOCKETIO_PORT = 8081
