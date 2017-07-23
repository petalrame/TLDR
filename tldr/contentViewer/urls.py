from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^api/$', views.dbGet, name="getAllData"),
	url(r'^[a-zA-Z0-9]*$', views.loadSite, name="index"),
]
