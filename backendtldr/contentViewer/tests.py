from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User

import datetime
import logging
import random

from summarize.models import Event
from .serializers import EventSerializer

# Create your tests here.
class UserTestCase(TestCase):
	
	def setUp(self):
		User.objects.create_user(username="cat", email="cat@yahoo.com", password="george")
		User.objects.create_user(username="cat1", email="cat1@yahoo.com", password="george1")
		User.objects.create_user(username="cat2", email="cat2@yahoo.com", password="george2")

	def test_user_register(self):
		client = APIClient()
		logger = logging.getLogger(__name__)

		response = self.client.post('/api/users/' , {'username': 'bob', 'email': 'bob@gmail.com', 'password': 'bobiscool'})

		if (response.status_code == 404):
			logger.warning(response)

		usr = User.objects.get(username="bob")

		self.assertEqual(usr.username, "bob")

	def test_user_login(self):
		client = APIClient()
		logger = logging.getLogger(__name__)

		response = self.client.post('/api/users/0/login/' , {'username': 'cat', 'password': 'george'})
		
		#should be a successful login

		response = self.client.post('/api/users/0/login/' , {'username': 'cat1', 'password': 'george'})

		#should be a failed login

	def test_user_login_then_logout(self):
		client = APIClient()
		logger = logging.getLogger(__name__)

		response = self.client.post('/api/users/0/login/' , {'username': 'cat2', 'password': 'george2'})
		
		#should be a successful login

		#log user out
		response = self.client.post('/api/users/0/logout/')

		

class InteractionsTestCase(TestCase):

	now = datetime.datetime.now()

	def setUp(self):
		#Create objects for testing

		Event.objects.create(title="Meow", ranking=1, summary="Who really cares?", lastedited=self.now, dateadded = datetime.datetime(2017, 4, 11, 12, 6, 5), clicktraffic=22, tags=["Politics"])
		Event.objects.create(title="Meow", ranking=3, summary="Who really cares?", lastedited=self.now, dateadded = datetime.datetime(2017, 5, 11, 12, 6, 5), clicktraffic=82, tags=["Economy"])
		Event.objects.create(title="Meow", ranking=2, summary="Who really cares?", lastedited=self.now, dateadded = datetime.datetime(2017, 5, 15, 12, 6, 5), clicktraffic=31, tags=["Tech"])
		Event.objects.create(title="Meow", ranking=6, summary="Who really cares?", lastedited=self.now, dateadded = datetime.datetime(2015, 7, 11, 12, 6, 5), clicktraffic=5, tags=["Fashion"])
		Event.objects.create(title="Meow", ranking=4, summary="Who really cares?", lastedited=self.now, dateadded = datetime.datetime(2017, 4, 1, 12, 6, 5), clicktraffic=97, tags=["Crime"])
		Event.objects.create(title="Meow", ranking=5, summary="Who really cares?", lastedited=self.now, dateadded = datetime.datetime(2013, 5, 2, 12, 6, 5), clicktraffic=1, tags=["Sports"])
		Event.objects.create(title="Meow", ranking=5, summary="Who really cares?", lastedited=self.now, dateadded = datetime.datetime(2017, 2, 3, 12, 6, 5), clicktraffic=1, tags=["Health"])
		Event.objects.create(title="Meow", ranking=1, summary="Who really cares?", lastedited=self.now, dateadded = datetime.datetime(2017, 1, 1, 12, 6, 5), clicktraffic=29, tags=["Politics"])
		Event.objects.create(title="Meow", ranking=43, summary="Who really cares?", lastedited=self.now, dateadded = datetime.datetime(2016, 12, 1, 12, 6, 5), clicktraffic=81, tags=["Economy"])
		Event.objects.create(title="Meow", ranking=8, summary="Who really cares?", lastedited=self.now, dateadded = datetime.datetime(2016, 2, 11, 12, 6, 5), clicktraffic=38, tags=["Tech"])
		Event.objects.create(title="Meow", ranking=6, summary="Who really cares?", lastedited=self.now, dateadded = datetime.datetime(2016, 3, 11, 12, 6, 5), clicktraffic=50, tags=["Fashion"])
		Event.objects.create(title="Meow", ranking=4, summary="Who really cares?", lastedited=self.now, dateadded = datetime.datetime(2016, 4, 11, 12, 6, 5), clicktraffic=9, tags=["Crime"])
		Event.objects.create(title="Meow", ranking=5, summary="Who really cares?", lastedited=self.now, dateadded = datetime.datetime(2016, 5, 11, 12, 6, 5), clicktraffic=11, tags=["Sports"])
		Event.objects.create(title="Meow", ranking=5, summary="Who really cares?", lastedited=self.now, dateadded = datetime.datetime(2016, 6, 11, 12, 6, 5), clicktraffic=111, tags=["Health"])


	def test_most_popular(self):
		client = APIClient()
		logger = logging.getLogger(__name__)

		response = self.client.get('/api/most_popular/')
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.order_by('-ranking')
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

		data = Event.objects.order_by('-clicktraffic')
		serializer = EventSerializer(data, many=True)	

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)

	def test_most_recent(self):
		client = APIClient()
		logger = logging.getLogger('django')

		response = self.client.get('/api/most_recent/')
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.order_by('-dateadded')
		serializer = EventSerializer(data, many=True)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)

	def test_get_content_by_tag_name(self):
		client = APIClient()
		logger = logging.getLogger(__name__)

		#politics tag
		response = self.client.get('/api/get_content_by_tag_name/', {'tag': 'Politics', 'order': 1})
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.filter(tags='Politics').order_by('-ranking')
		serializer = EventSerializer(data, many=True)	

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)

		#economy tag
		response = self.client.get('/api/get_content_by_tag_name/', {'tag': 'Economy', 'order': 1})
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.filter(tags='Economy').order_by('-ranking')
		serializer = EventSerializer(data, many=True)	

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)

		#tech tag
		response = self.client.get('/api/get_content_by_tag_name/', {'tag': 'Tech', 'order': 2})
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.filter(tags='Tech').order_by('-clicktraffic')
		serializer = EventSerializer(data, many=True)	

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)

		#Sports tag
		response = self.client.get('/api/get_content_by_tag_name/', {'tag': 'Sports', 'order': 2})
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.filter(tags='Sports').order_by('-clicktraffic')
		serializer = EventSerializer(data, many=True)	

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)

		#fashion tag
		response = self.client.get('/api/get_content_by_tag_name/', {'tag': 'Fashion', 'order': 2})
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.filter(tags='Fashion').order_by('-clicktraffic')
		serializer = EventSerializer(data, many=True)	

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)

		#crime tag
		response = self.client.get('/api/get_content_by_tag_name/', {'tag': 'Crime', 'order': 3})
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.filter(tags='Crime').order_by('-dateadded')
		serializer = EventSerializer(data, many=True)	

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.content_type, 'json')
		self.assertEqual(response.data, serializer.data)

		#health tag
		response = self.client.get('/api/get_content_by_tag_name/', {'tag': 'Health', 'order': 3})
		if (response.status_code == 404):
			logger.warning(response)

		data = Event.objects.filter(tags='Health').order_by('-dateadded')
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

