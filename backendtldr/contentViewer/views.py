from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route, list_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import logging
from django.contrib.auth import login, logout, authenticate

from summarize.models import Event
from django.contrib.auth.models import User
from .serializers import EventSerializer, UserSerializer

# Create your views here.

def loadSite(request):
	return render(request, 'contentViewer/index.html')

class UserAccountViewSet(viewsets.ViewSet):

	#Register and Create User
	def create(self, request):
		username = request.data.get("username")
		password = request.data.get("password")
		email = request.data.get("email")

		#create user
		user = User.objects.create_user(username=username, email=email, password=password)

		#log user in
		login_result = authenticate(request, username=username, password=password)
		if login_result is not None:
			#user authenticated. log user in
			login(request, login_result)
		else:
			#error user not authenticated
			return Response(status=status.HTTP_401_UNAUTHORIZED)
			

		serializer = UserSerializer(user)		#Serialize data
		#json = JSONRenderer().render(serializer.data)
		#return Response(serializer.data, status=status.HTTP_200_OK)
		return redirect("/")

	#login User
	@detail_route(methods=['POST'])
	def login(self, request, pk=None):
		username = request.data.get("username")
		password = request.data.get("password")

		#log user in
		user = authenticate(request, username=username, password=password)
		if user is not None:
			#user authenticated. log user in
			login(request, user)
		else:
			#error user not authenticated
			return Response(status=status.HTTP_401_UNAUTHORIZED)
			

		serializer = UserSerializer(user)		#Serialize data
		#json = JSONRenderer().render(serializer.data)
		#return Response(serializer.data, status=status.HTTP_200_OK)
		return redirect("/")


	#logout User
	@detail_route(methods=["POST"])
	def logout(self, request, pk=None):
		logout(request)
		return Response(status=status.HTTP_200_OK)
	
		
	@detail_route(methods=['GET'])
	def login_status(self, request, pk=None):
		if request.user.is_authenticated:
			return Response({'login_status': 1}, status=status.HTTP_200_OK)
		else:
			return Response({'login_status': 0}, status=status.HTTP_200_OK)
			

	
class UserInteractionsViewSet(viewsets.ViewSet):
	"""
	ViewSet for retreiving data from Event Table. Updating
	like counter in Event Table.
	"""

	#Gets most popular data in table based on ranking
	@list_route(methods=['GET'])
	def most_popular(self, request):
		data = Event.objects.order_by('-ranking')	#Gets data based on numLikes
		serializer = EventSerializer(data, many=True)		#Serialize data

		return Response(serializer.data, content_type='json')	#Return JSON serialized data

	#Gets most viewed data, data with most clicktraffic
	@list_route(methods=['GET'])
	def most_viewed(self, request):
		data = Event.objects.order_by('-clicktraffic')
		serializer = EventSerializer(data, many=True)		

		return Response(serializer.data, content_type='json')


	#Gets most recent data, data with most recent dateadded field
	@list_route(methods=['GET'])
	def most_recent(self, request):
		data = Event.objects.order_by('-dateadded')
		serializer = EventSerializer(data, many=True)

		return Response(serializer.data, content_type='json')

	@list_route(methods=['GET'])
	def get_content_by_tag_name(self, request):
		requestdata = request.query_params	#contains data sent by client
		tag = requestdata['tag']
		order = int(requestdata['order'])

		if (order == 1):
			data = Event.objects.filter(tags=tag).order_by('-ranking')
		elif (order == 2):
			data = Event.objects.filter(tags=tag).order_by('-clicktraffic')
		elif (order == 3):
			data = Event.objects.filter(tags=tag).order_by('-dateadded')

		serializer = EventSerializer(data, many=True)

		return Response(serializer.data, content_type="json")

	@detail_route(methods=['POST'])
	def like(self, request, pk):
		logger = logging.getLogger('django')
		logger.info("meowman")
		likeUpdate = int(request.data['likestatus'])		#like or dislike
		logger.info(likeUpdate)

		#updates Element Ranking based on like or dislike
		elementToUpdate = Event.objects.get(id=pk)
		elementToUpdate.ranking = elementToUpdate.ranking + likeUpdate
		elementToUpdate.save()

		return Response(status=status.HTTP_200_OK)

	@detail_route(methods=['GET'])
	def get_entry(self, request, pk):
		entry = Event.objects.get(id=pk)

		serializer = EventSerializer(entry)

		return Response(serializer.data, content_type="json")
