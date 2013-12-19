from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from quickdraw.donations.models import Donation
from datetime import datetime, timedelta
import stripe

stripe.api_key = settings.STRIPE_SECRET

def donate(request):
	result = stripe.Charge.create(
		amount = 300,
		currency = 'gbp',
		card = request.GET.get('token'),
		metadata = {
			'site': Site.objects.get_current().name
		}
	)
	
	Donation.objects.create(
		remote_id = result['id'],
		live = result['livemode'],
		paid = result['paid'],
		amount = result['amount'] / 100,
		currency = result['currency'],
		created = datetime(1970, 1, 1, 0, 0, 0) + timedelta(seconds = result['created'])
	)
	
	messages.success(request, u'Thank you for your donation!')
	return HttpResponseRedirect(
		request.GET.get('next', 'thanks/')
	)

def thanks(request):
	return TemplateResponse(
		request,
		'donations/thanks.html',
		{}
	)