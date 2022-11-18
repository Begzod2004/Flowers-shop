from rest_framework import serializers
from apps.order.models import *


class Weight_cargoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weight_cargo
        fields ='__all__'



class Volume_cargoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Volume_cargo
        fields ='__all__'



class Type_cargoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type_cargo
        fields ='__all__'



class Mode_cargoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mode_cargo
        fields ='__all__'



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'car',
            'title',
            'date_created',
            'from_here',
            'to_here',
            'phone_number',
            'weight_cargo',
            'volume_cargo',
            'type_cargo',
            'mode_cargo',
            'images',
            'images2',
            'images3',
        )
class OrdergetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            'car',
            'title',
            'date_created',
            'from_here',
            'to_here',
            'phone_number',
            'weight_cargo',
            'volume_cargo',
            'type_cargo',
            'mode_cargo',
            'images',
            'images2',
            'images3',
        )