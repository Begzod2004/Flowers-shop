from django.shortcuts import get_object_or_404, render

import json
from rest_framework import viewsets
from apps.products.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import generics
from django_filters import rest_framework as filters
# Create your views here.

    # def get_queryset(self):
    #     products = Product.objects.filter(draft=False).annotate(
    #         middle_star=models.Sum(models.F('ratings__rating_score')) / models.Count(models.F('ratings'))
    #     )
    #     return products

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return CreateRatingSerializer

@api_view(['GET'])
def Product_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=ProductSerializer(instance=Product.objects.all(), many=True).data, status=200)
        else:
            the_Product = get_object_or_404(Product, pk=pk)
            return Response(data=ProductSerializer(instance=the_Product).data, status=200)
   
    
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReviewaSerializer
    # serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (FormParser, MultiPartParser)


@api_view(['GET'])
def Image_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=ImageSerializer(instance=Image.objects.all(), many=True).data, status=200)
        else:
            the_Image = get_object_or_404(Image, pk=pk)
            return Response(data=ImageSerializer(instance=the_Image).data, status=200)
   

class ImageListAPIView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageCreateAPIView(CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (FormParser, MultiPartParser)


@api_view(['GET'])
def Color_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=ColorSerializer(instance=Color.objects.all(), many=True).data, status=200)
        else:
            the_Color = get_object_or_404(Color, pk=pk)
            return Response(data=ColorSerializer(instance=the_Color).data, status=200)
   

class ColorListAPIView(ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ColorCreateAPIView(CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    parser_classes = (FormParser, MultiPartParser)


@api_view(['GET'])
def Flower_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=FlowerSerializer(instance=Flower.objects.all(), many=True).data, status=200)
        else:
            the_Flower = get_object_or_404(Flower, pk=pk)
            return Response(data=FlowerSerializer(instance=the_Flower).data, status=200)
   

class FlowerListAPIView(ListAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer


class FlowerCreateAPIView(CreateAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    parser_classes = (FormParser, MultiPartParser)


@api_view(['GET'])
def ProductReview_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=ProductReviewSerializer(instance=ProductReview.objects.all(), many=True).data, status=200)
        else:
            the_ProductReview = get_object_or_404(ProductReview, pk=pk)
            return Response(data=ProductReviewSerializer(instance=the_ProductReview).data, status=200)
   

class ProductReviewListAPIView(ListAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer


class ProductReviewCreateAPIView(CreateAPIView):
    queryset = ProductReview.objects.all()
    parser_classes = (FormParser, MultiPartParser)    
