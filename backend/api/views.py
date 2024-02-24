from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.
@api_view(['GET'])
def api_home(request):
    data = {}
    instance = Product.objects.all().order_by('?').first()
    if instance:
        # data = model_to_dict(instance, fields=['id', 'title', 'price'])
        data = ProductSerializer(instance).data
    return Response(data)

@api_view(['POST'])
def put_api(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # print(serializer.data)
        instance = serializer.save()
        return Response(ProductSerializer(instance).data)
    return Response({"Response": "Invalid Data"})

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