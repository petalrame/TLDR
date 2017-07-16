from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

class Event(models.Model):
	title = models.CharField(max_length = 200)
	ranking = models.PositiveIntegerField()
	summary = models.TextField()
	#TODO: Foreign Key relationship with articles
	lastedited = models.DateTimeField(auto_now=False, auto_now_add=False)
	clicktraffic = models.PositiveIntegerField()
	tags = ArrayField(models.CharField(max_length=50))
