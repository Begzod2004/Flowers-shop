import jwt
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.db.models import Q
from django.utils.encoding import smart_bytes, smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from drf_yasg import openapi
from rest_framework import generics, status, views
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import json
from apps.news.models import New
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *
from rest_framework.parsers import FormParser, MultiPartParser
# Create your views here.

@api_view(['GET'])
def News_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=NewsSerializer(instance=New.objects.all(), many=True).data, status=200)
        else:
            the_New = get_object_or_404(New, pk=pk)
            return Response(data=NewsSerializer(instance=the_New).data, status=200)

class NewsListAPIView(ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewsSerializer
    parser_classes = (FormParser, MultiPartParser)   


class NewsCreateAPIView(CreateAPIView):
    queryset = New.objects.all()
    serializer_class = NewsSerializer
    parser_classes = (FormParser, MultiPartParser)   

