from rest_framework import serializers
from apps.order.models import Cart


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Cart
        fields = ["id"]
