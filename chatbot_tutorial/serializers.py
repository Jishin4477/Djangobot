from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import AllCalls, GetUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class AllCallsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = AllCalls
        fields = "__all__"

class GetUserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = GetUser
        fields = "__all__"