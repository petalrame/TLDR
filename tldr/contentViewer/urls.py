from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'api', views.UserInteractionsViewSet, base_name="user_interaction")

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^[a-zA-Z0-9]*$', views.loadSite, name="index"),
]
