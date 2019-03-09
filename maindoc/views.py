# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse,Http404

# config = {
#     'apiKey': "AIzaSyArtJ-cIfgFq44XVpGQ3dc-4-VRSw4hT1k",
#     'authDomain': "docconnect-f68fa.firebaseapp.com",
#     'databaseURL': "https://docconnect-f68fa.firebaseio.com",
#     'projectId': "docconnect-f68fa",
#     'storageBucket': "docconnect-f68fa.appspot.com",
#     'messagingSenderId': "691566246296"
# }
# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()

def index(request):
    return render(request, 'index.html')


def signin(request):
    return render(request, 'contact.html')


# @csrf_exempt
# @require_http_methods(['POST'])
# def postsignin(request):
#     data = request.POST
#     response = {}
#     try:
#         user = data['user']
#         response['status'] = 1
#     except:
#         response['status'] = 0
#     return JsonResponse(response)
