# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-05 01:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contentViewer', '0003_auto_20170904_0242'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='dateadded',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
