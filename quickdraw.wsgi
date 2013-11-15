try:
	import newrelic.agent
	newrelic.agent.initialize('newrelic.ini')
except ImportError:
	pass

import os, sys

sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quickdraw.settings')
os.environ['PYTHON_EGG_CACHE'] = os.path.dirname(__file__) + '/.python-eggs'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()