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
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import json
from apps.order.models import Order
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import FormParser, MultiPartParser
# Create your views here.

@api_view(['GET'])
def Order_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=OrdergetSerializer(instance=Order.objects.all(), many=True).data, status=200)
        else:
            the_Order = get_object_or_404(Order, pk=pk)
            return Response(data=OrdergetSerializer(instance=the_Order).data, status=200)
       

class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrdergetSerializer


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    parser_classes =  (FormParser, MultiPartParser,FileUploadParser)


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

