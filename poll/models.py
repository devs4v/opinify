from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from model_utils.fields import StatusField
from model_utils import Choices

class Poll(TimeStampedModel):
	"""Poll model manages the individual polls"""
	LIVE_STATUS = Choices('draft', 'live')

	title = models.CharField(max_length=500)
	creator = models.ForeignKey(settings.AUTH_USER_MODEL)
	expires = models.DateTimeField()

	islive = StatusField(choices_name='LIVE_STATUS')

	def save_to_firebase(self):
		pass

	def _serialize_to_json(self):
		pass
		
		
class Options(models.Model):
	""" Options for each of the poll presented to user"""

	poll = models.ForeignKey(Poll)
	label = models.CharField(max_length=500)

	def save_to_firebase(self):
		pass
		
	def _serialize_to_json(self):
		pass

class Vote(TimeStampedModel):
	""" Each of the votes """

	voter = models.ForeignKey(settings.AUTH_USER_MODEL)
	vote = models.ForeignKey(Options)

	def save_to_firebase(self):
		pass

	def _serialize_to_json(self):
		pass
