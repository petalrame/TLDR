from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

import datetime
import logging
import random

from .models import Event
from .serializers import EventSerializer

# Create your tests here.
class UserInteractionsTestCase(TestCase):

	now = datetime.datetime.now()

	def setUp(self):
		#Create objects for testing

		Event.objects.create(title="Meow", ranking=1, summary="Who really cares?", lastedited=self.now, clicktraffic=22, tags=["Politics"])
		Event.objects.create(title="Meow", ranking=3, summary="Who really cares?", lastedited=self.now, clicktraffic=82, tags=["Economy"])
		Event.objects.create(title="Meow", ranking=2, summary="Who really cares?", lastedited=self.now, clicktraffic=31, tags=["Tech"])
		Event.objects.create(title="Meow", ranking=6, summary="Who really cares?", lastedited=self.now, clicktraffic=5, tags=["Fashion"])
		Event.objects.create(title="Meow", ranking=4, summary="Who really cares?", lastedited=self.now, clicktraffic=97, tags=["Crime"])
		Event.objects.create(title="Meow", ranking=5, summary="Who really cares?", lastedited=self.now, clicktraffic=1, tags=["Sports"])
		Event.objects.create(title="Meow", ranking=5, summary="Who really cares?", lastedited=self.now, clicktraffic=1, tags=["Health"])
		Event.objects.create(title="Meow", ranking=1, summary="Who really cares?", lastedited=self.now, clicktraffic=29, tags=["Politics"])
		Event.objects.create(title="Meow", ranking=43, summary="Who really cares?", lastedited=self.now, clicktraffic=81, tags=["Economy"])
		Event.objects.create(title="Meow", ranking=8, summary="Who really cares?", lastedited=self.now, clicktraffic=38, tags=["Tech"])
		Event.objects.create(title="Meow", ranking=6, summary="Who really cares?", lastedited=self.now, clicktraffic=50, tags=["Fashion"])
		Event.objects.create(title="Meow", ranking=4, summary="Who really cares?", lastedited=self.now, clicktraffic=9, tags=["Crime"])
		Event.objects.create(title="Meow", ranking=5, summary="Who really cares?", lastedited=self.now, clicktraffic=11, tags=["Sports"])
		Event.objects.create(title="Meow", ranking=5, summary="Who really cares?", lastedited=self.now, clicktraffic=111, tags=["Health"])


	def test_most_popular(self):
		client = APIClient()
		logger = logging.getLogger(__name__)

		response = self.client.get('/api/most_popular/')
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.order_by('ranking')
		serializer = EventSerializer(data, many=True)	

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
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
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)

	def test_get_content_by_tag_name(self):
		client = APIClient()
		logger = logging.getLogger(__name__)

		#politics tag
		response = self.client.get('/api/get_content_by_tag_name/', {'tag': 'Politics'})
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.filter(tags__contains=['Politics'])
		serializer = EventSerializer(data, many=True)	

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)

		#economy tag
		response = self.client.get('/api/get_content_by_tag_name/', {'tag': 'Economy'})
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.filter(tags__contains=['Economy'])
		serializer = EventSerializer(data, many=True)	

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)

		#tech tag
		response = self.client.get('/api/get_content_by_tag_name/', {'tag': 'Tech'})
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.filter(tags__contains=['Tech'])
		serializer = EventSerializer(data, many=True)	

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)

		#Sports tag
		response = self.client.get('/api/get_content_by_tag_name/', {'tag': 'Sports'})
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.filter(tags__contains=['Sports'])
		serializer = EventSerializer(data, many=True)	

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)

		#fashion tag
		response = self.client.get('/api/get_content_by_tag_name/', {'tag': 'Fashion'})
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.filter(tags__contains=['Fashion'])
		serializer = EventSerializer(data, many=True)	

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)

		#crime tag
		response = self.client.get('/api/get_content_by_tag_name/', {'tag': 'Crime'})
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.filter(tags__contains=['Crime'])
		serializer = EventSerializer(data, many=True)	

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)

		#health tag
		response = self.client.get('/api/get_content_by_tag_name/', {'tag': 'Health'})
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.filter(tags__contains=['Health'])
		serializer = EventSerializer(data, many=True)	

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)

	def test_send_like_or_dislike(self):
		client = APIClient()
		logger = logging.getLogger(__name__)

		random_idx = random.randint(0, Event.objects.count() - 1)
		random_obj_id = Event.objects.all()[random_idx].id

		previousLikeStatus = Event.objects.get(id=random_obj_id).ranking	#ranking before request

		response = self.client.post('/api/' + str(random_obj_id) + '/like/', {'likestatus': 1})

		currentLikeStatus = Event.objects.get(id=random_obj_id).ranking	#ranking after request

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(currentLikeStatus, previousLikeStatus + 1)

		previousLikeStatus = Event.objects.get(id=random_obj_id).ranking	#ranking before request

		response = self.client.post('/api/' + str(random_obj_id) + '/like/', {'likestatus': -1})

		currentLikeStatus = Event.objects.get(id=random_obj_id).ranking	#ranking after request

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(currentLikeStatus, previousLikeStatus - 1)

	def test_get_entry(self):
		client = APIClient()
		logger = logging.getLogger(__name__)
		
		random_idx = random.randint(0, Event.objects.count() - 1)
		random_obj_id = Event.objects.all()[random_idx].id

		response = self.client.get('/api/' + str(random_obj_id) + '/get_entry/')
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.get(id=random_obj_id)
		serializer = EventSerializer(data)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)

