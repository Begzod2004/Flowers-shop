from rest_framework import serializers
from apps.order.models import Order,OrderItem
from apps.account.api.v1.serializers import AccountSerializer
from apps.products.api.v1.serializers import ProductWatchSerializer
from apps.products.models import Product
from django.db import transaction


class OrderItemSerializer(serializers.ModelSerializer):
    # product = ProductReviewaSerializer()
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderItemWatchSerializer(serializers.ModelSerializer):
    product = ProductWatchSerializer()

    class Meta:
        model = OrderItem
        fields = ('id','product','count')


class OrderWatchSerializer(serializers.ModelSerializer):
    user = AccountSerializer()
    orderitem = OrderItemWatchSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ('id','user','code','orderitem',)

class OrderItemCkeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('product','count')


class OrderSerializer(serializers.ModelSerializer):
    orderitem = OrderItemCkeckSerializer(many=True)

    # def validate(self, attrs):
    #     orderitems = self.context.get("orderitem")
    #     if orderitems:
    #         orderitem_ser = OrderItemCkeckSerializer(data = orderitems,many=True)
    #         orderitem_ser.is_valid(raise_exception=True)
    #         return attrs
    #     raise serializers.ValidationError({"Error":"orderitems must be given"})

    # mahmud:900463836

    def create(self, validated_data):
        user_id = self.context.get('user')
        tracks_data = validated_data.pop('orderitem')
        order = Order.objects.create(user=user_id,**validated_data)
        for track_data in tracks_data:

            OrderItem.objects.create(order=order, **track_data)
        return order
        # orderitems = self.context.get("orderitem")
        # with transaction.atomic():
        #     order = Order.objects.create(**validated_data)
        #     for item in orderitems:
        #         product = Product.objects.get(id=item.get('product'))
        #         OrderItem.objects.create(order=order,
        #                                     product=product,
        #                                     count=item.get('count'))
        # return order
    
    class Meta:
        model = Order
        fields = ('id','orderitem',)


class OrderDetailSerializer(serializers.ModelSerializer):
    orderitem = OrderItemWatchSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ('id','user','code','status','orderitem',)


