from __future__ import unicode_literals
from django.db import models
import tagulous
import tagulous.models


class Article(models.Model):
    title = models.CharField(max_length=150)
    authors = models.CharField(max_length=200)
    content = models.CharField(max_length=90000)
    url = models.CharField(max_length=300)
    date = models.DateTimeField('date')
    tags = models.CharField(max_length=300)


    class Meta():
        app_label = 'scraper'
