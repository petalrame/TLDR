from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def loadSite(request):
	return HttpResponse("Ram Sucks")

"""This function fetches information from the database"""
def dbGet(request):
    return null

"""This function posts data to the database"""
def dbPost(request):
    return null
