from django.conf import settings as s

def settings(request):
	return {
		'STRIPE_KEY': s.STRIPE_KEY
	}