from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Todo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name']


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'created_at', 'user', 'time_passed'] # time_passed ist eine eigene Variable/Funktion die in models deklariert ist