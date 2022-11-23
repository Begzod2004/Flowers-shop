from rest_framework import viewsets, mixins
from apps.products.api.v1.filters import *
from apps.products.api.v1.serializers import *
from apps.products.models import Product


class ProductViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductFilterSerializer
    filterset_class = ProductFilter


