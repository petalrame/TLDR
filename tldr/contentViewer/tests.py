from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

import datetime
import logging

from .models import Event
from .serializers import EventSerializer

# Create your tests here.
class UserInteractionsTestCase(TestCase):

	now = datetime.datetime.now()

	def setUp(self):
		#Create objects for testing

		Event.objects.create(title="Meow", ranking=1, summary="Who really cares?", lastedited=self.now, clicktraffic=22, tags=["Politics"])
		Event.objects.create(title="Meow", ranking=3, summary="Who really cares?", lastedited=self.now, clicktraffic=82, tags=["Politics"])
		Event.objects.create(title="Meow", ranking=2, summary="Who really cares?", lastedited=self.now, clicktraffic=31, tags=["Politics"])
		Event.objects.create(title="Meow", ranking=6, summary="Who really cares?", lastedited=self.now, clicktraffic=5, tags=["Politics"])
		Event.objects.create(title="Meow", ranking=4, summary="Who really cares?", lastedited=self.now, clicktraffic=97, tags=["Politics"])
		Event.objects.create(title="Meow", ranking=5, summary="Who really cares?", lastedited=self.now, clicktraffic=1, tags=["Politics"])

	def test_most_popular(self):
		client = APIClient()
		logger = logging.getLogger(__name__)

		response = self.client.get('/api/most_popular/')
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.order_by('ranking')
		serializer = EventSerializer(data, many=True)	

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data, serializer.data)
		
	def test_most_viewed(self):	
		client = APIClient()
		logger = logging.getLogger(__name__)

		response = self.client.get('/api/most_viewed/')
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.order_by('clicktraffic').reverse()
		serializer = EventSerializer(data, many=True)	

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data, serializer.data)
		

