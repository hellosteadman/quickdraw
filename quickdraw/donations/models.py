from django.db import models

class Donation(models.Model):
	remote_id = models.CharField(max_length = 32)
	live = models.BooleanField(default = False)
	paid = models.BooleanField(default = False)
	amount = models.DecimalField(decimal_places = 2, max_digits = 5)
	currency = models.CharField(max_length = 3)
	created = models.DateTimeField()
	
	def __unicode__(self):
		return self.remote_id