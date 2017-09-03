from __future__ import unicode_literals

from django.db import models

class article(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=50)
    content = models.CharField(max_length=2000)
    date = models.DateTimeField('date')


