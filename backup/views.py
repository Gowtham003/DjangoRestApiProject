from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
def api_home(request):
    return JsonResponse({"message": "This is Django API response!"})

def echo_echo(request):
    data = {}
    print(request)
    body = request.body
    try:
        data = json.loads(body)
    except:
        pass
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)