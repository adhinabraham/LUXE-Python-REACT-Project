from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from django.http import Http404
from .models import Cart
from .serilazer import MycartSerializer

# Create your views here.
class Addcart(APIView):
    def post (self,request,pk):
        pass

