# Create tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery import Celery

app = Celery('tasks', broker='redis://localhost')

@shared_task
def scrape():
    # Test task
    print("Running task")