import django_filters as filters
from apps.products.models import *


class ProductFilter(filters.FilterSet):
    price_gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = filters.NumberFilter(field_name='price', lookup_expr='lt')

  
# class TypeFilter(filters.FilterSet):
#     class Meta:
#         model = Product
#         fields = ['']
