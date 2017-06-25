from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the tldr index.")

"""This function fetches information from the database"""
def dbGet(request):
    return null

"""This function posts data to the database"""
def dbPost(request):
    return null
