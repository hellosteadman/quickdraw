from django.contrib.auth import logout as log_out
from django.http import HttpResponseRedirect

def logout(request):
	log_out(request)
	return HttpResponseRedirect('/')