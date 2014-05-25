from bambu import cron
from django.utils.timezone import now
from django.conf import settings
from django.contrib.sites.models import Site
from twitter import Twitter, OAuth
from social_auth.models import UserSocialAuth
from quickdraw.qanda.models import Question, Answer, Vote
from bambu_urlshortener import shorten

class QuestionJob(cron.CronJob):
	frequency = cron.MINUTE

	def run(self, logger):
		date = now()
		domain = Site.objects.get_current().domain

		for question in Question.objects.filter(closes__lte = date, tweeted = False):
			access = UserSocialAuth.objects.get(
				user = question.creator,
				provider = 'twitter'
			).tokens

			tweet = 'The results of the snap %s are in! %s Create your own at http://%s/' % (
				question.get_kind_display(),
				shorten(
					'http://%s%s' % (
						domain,
						question.get_absolute_url()
					)
				),
				domain
			)

			api = Twitter(
				auth = OAuth(
					access['oauth_token'],
					access['oauth_token_secret'],
					settings.TWITTER_CONSUMER_KEY,
					settings.TWITTER_CONSUMER_SECRET
				)
			)

			question.tweeted = True
			question.save()
			api.statuses.update(status = tweet)

cron.site.register(QuestionJob)
