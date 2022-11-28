from rest_framework import serializers
from apps.order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Order
        fields = ['id','user_id','status','product','created']
