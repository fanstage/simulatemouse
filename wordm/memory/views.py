from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
class MySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    message = serializers.CharField()


@api_view(['GET'])
def my_view(request):
    data = {'message': 'hello world'}
    return Response(data)
# Create your views here.
