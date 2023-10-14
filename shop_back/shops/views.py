from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import TovarSerializer, CatSerializer


@api_view(['GET'])
def API_View(request):
    if request.method == 'GET':
        tov = Tovar.objects.all()
        serializer = TovarSerializer(tov, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def API_View_D(request, id):
    if request.method == 'GET':
        t = Tovar.objects.get(id=id)
        serializer = TovarSerializer(t)
        return Response(serializer.data)


@api_view(['GET'])
def API_list(request, cat_id):
    if request.method == 'GET':
        cats = Tovar.objects.filter(cat_id=cat_id)
        serializer = TovarSerializer(cats, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def API_cat(request):
    if request.method == 'GET':
        cat = Category.objects.all()
        serializer = CatSerializer(cat, many=True)
        return Response(serializer.data)


# Create your views here.
