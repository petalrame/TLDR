from summarize.models import Event
from rest_framework import serializers
from django.contrib.auth.models import User

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('pk', 'username', 'first_name', 'last_name')
