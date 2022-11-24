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



@api_view(['GET'])
def Gallery_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=GallerySerializer(instance=Gallery.objects.all(), many=True).data, status=200)
        else:
            the_Gallery = get_object_or_404(Gallery, pk=pk)
            return Response(data=GallerySerializer(instance=the_Gallery).data, status=200)
   

class GalleryListAPIView(ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class GalleryCreateAPIView(CreateAPIView):
    queryset = Gallery.objects.all()
    parser_classes = (FormParser, MultiPartParser)    



@api_view(['GET'])
def Sections_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=SectionsSerializer(instance=Sections.objects.all(), many=True).data, status=200)
        else:
            the_Sections = get_object_or_404(Sections, pk=pk)
            return Response(data=SectionsSerializer(instance=the_Sections).data, status=200)
   

class SectionsListAPIView(ListAPIView):
    queryset = Sections.objects.all()
    serializer_class = SectionsSerializer


class SectionsCreateAPIView(CreateAPIView):
    queryset = Sections.objects.all()
    parser_classes = (FormParser, MultiPartParser)    




@api_view(['GET'])
def SectionsCategory_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=SectionsCategorySerializer(instance=SectionsCategory.objects.all(), many=True).data, status=200)
        else:
            the_SectionsCategory = get_object_or_404(SectionsCategory, pk=pk)
            return Response(data=SectionsCategorySerializer(instance=the_SectionsCategory).data, status=200)
   

class SectionsCategoryListAPIView(ListAPIView):
    queryset = SectionsCategory.objects.all()
    serializer_class = SectionsCategorySerializer


class SectionsCategoryCreateAPIView(CreateAPIView):
    queryset = SectionsCategory.objects.all()
    parser_classes = (FormParser, MultiPartParser)    
