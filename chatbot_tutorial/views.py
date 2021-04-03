from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, GetUserSerialiser
from rest_framework.response import Response
import json
import requests
import random
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from chatbot_tutorial.models import AllCalls, GetUser
from django.template.loader import render_to_string
from .serializers import AllCallsSerialiser
from datetime import datetime


def chat(request):
    print("entered first")
    print(request.user)
    get_user, created = GetUser.objects.get_or_create(user=request.user)
    user_data = GetUser.objects.get(user=request.user)
    user_data.date = datetime.now()
    user_data.save()
    context = {}
    return render(request, 'chatbot_tutorial/chatbot.html', context)


def respond_to_websockets(message):

    print("entered here")

    jokes = {
    'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
    'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
    'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] 
    }  

    result_message = {
        'type': 'text'
    }


    if 'fat' in message['text']:
        result_message['text'] = random.choice(jokes['fat'])
        user = GetUser.objects.all().order_by('-date').first()
        fat_click = AllCalls.objects.create(entered_val=message['text'], user=user.user)
        
    
    elif 'stupid' in message['text']:
        result_message['text'] = random.choice(jokes['stupid'])
        user = GetUser.objects.all().order_by('-date').first()
        stupid_data = AllCalls.objects.create(entered_val=message['text'], user=user.user)
    
    elif 'dumb' in message['text']:
        result_message['text'] = random.choice(jokes['dumb'])
        user = GetUser.objects.all().order_by('-date').first()
        dumb_data = AllCalls.objects.create(entered_val=message['text'], user=user.user)

    elif message['text'] in ['hi', 'hey', 'hello']:
        result_message['text'] = "Hello to you too! If you're interested in yo mama jokes, just tell me fat, stupid or dumb and i'll tell you an appropriate joke."
    else:
        result_message['text'] = "I don't know any responses for that. If you're interested in yo mama jokes tell me fat, stupid or dumb."
        
    return result_message
    
def show(request):
    get_user = GetUser.objects.all()
    context = []
    for user in get_user:       
        fat_data = AllCalls.objects.filter(entered_val__icontains='fat', user=user.user).count()
        stupid_data = AllCalls.objects.filter(entered_val__icontains='stupid', user=user.user).count()
        dumb_data = AllCalls.objects.filter(entered_val__icontains='dumb', user=user.user).count()
        context.append({
            "user": user, 'fat': fat_data, 'stupid': stupid_data, 'dumb': dumb_data
        })
    print(context)
    template = loader.get_template('chatbot_tutorial/all_data.html')
    response_body = template.render({"obj":context})
    return HttpResponse(response_body)

def clear(request):
    fat_data = AllCalls.objects.filter(entered_val__icontains='fat').delete()
    stupid_data = AllCalls.objects.filter(entered_val__icontains='stupid').delete()
    dumb_data = AllCalls.objects.filter(entered_val__icontains='dumb').delete()
    template = loader.get_template('chatbot_tutorial/clear_data.html')
    response_body = template.render()

    return HttpResponse(response_body)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]