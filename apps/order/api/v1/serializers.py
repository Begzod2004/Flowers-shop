from rest_framework import serializers
from apps.order.models import Order,OrderItem
from apps.account.api.v1.serializers import AccountSerializer
from apps.products.api.v1.serializers import ProductWatchSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    # product = ProductReviewaSerializer()
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderItemWatchSerializer(serializers.ModelSerializer):
    product = ProductWatchSerializer(many=True)

    class Meta:
        model = OrderItem
        fields = ('id','product','count')


class OrderWatchSerializer(serializers.ModelSerializer):
    user = AccountSerializer()
    orderitem = OrderItemWatchSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ('id','user','code','orderitem',)


class OrderSerializer(serializers.ModelSerializer):
    # user = AccountSerializer()
    
    class Meta:
        model = Order
        fields = ('id','user','code',)


