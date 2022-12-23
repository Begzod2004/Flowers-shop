import jwt
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.db.models import Q
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
from apps.order.models import Order
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *
from rest_framework.parsers import FormParser, MultiPartParser
from apps.account.models import Account
# Create your views here.


@api_view(['GET'])
def Order_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=OrderSerializer(instance=Order.objects.all(), many=True).data, status=200)
        else:
            the_Order = get_object_or_404(Order, pk=pk)
            return Response(data=OrderDetailSerializer(instance=the_Order).data, status=status.HTTP_200_OK)


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderWatchSerializer
    parser_classes = (FormParser, MultiPartParser)   


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes=[IsAuthenticated]
   
    def create(self, request, *args, **kwargs):
        orderitem = request.data.get("orderitem")
        data = request.data
        user = request.user
        # user = Account.objects.first()
        data['user'] = user
        serializer = self.get_serializer(data = data, context ={"user":user} )
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(data = serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class OrderItemListAPIView(ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    parser_classes = (FormParser, MultiPartParser)   


class OrderItemCreateAPIView(CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
