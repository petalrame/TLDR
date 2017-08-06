from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer

# Create your views here.

def loadSite(request):
	return render(request, 'contentViewer/index.html')

class UserInteractionsViewSet(viewsets.ViewSet):
	"""
	ViewSet for retreiving data from Event Table. Updating
	like counter in Event Table.
	"""

	#Gets most popular data in table based on ranking
	@list_route(methods=['GET'])
	def most_popular(self, request):
		data = Event.objects.order_by('ranking')	#Gets data based on numLikes
		serializer = EventSerializer(data, many=True)		#Serialize data

		return Response(serializer.data, content_type='json')	#Return JSON serialized data

	#Gets most viewed data, data with most clicktraffic
	@list_route(methods=['GET'])
	def most_viewed(self, request):
		data = Event.objects.order_by('clicktraffic').reverse()	
		serializer = EventSerializer(data, many=True)		

		return Response(serializer.data, content_type='json')
