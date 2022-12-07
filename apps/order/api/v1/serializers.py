from rest_framework import serializers
from apps.order.models import Order,OrderItem
from apps.products.api.v1.serializers import *



class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id','user',]

class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    order = OrdersSerializer()
    
    class Meta:
        model = OrderItem
        fields = ['order','product','count',]
