from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Event

# Create your views here.

def loadSite(request):
	return render(request, 'contentViewer/index.html')
	#return HttpResponse("Ram Sucks")

"""This function fetches information from the database"""
def dbGet(request):
	data = Event.objects.all()
	return JsonResponse({'entries': list(data)})

"""This function posts data to the database"""
def dbPost(request):
    return null
