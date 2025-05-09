from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view()
def story_list(request):
    return Response({'First_whistle':'Hello world!'})