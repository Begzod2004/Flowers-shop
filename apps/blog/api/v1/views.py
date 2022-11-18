from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import json
from apps.blog.models import Category, Blog
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *
from rest_framework.parsers import FormParser, MultiPartParser
# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Category_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=CategoryBlogSerializer(instance=Category.objects.all(), many=True).data, status=200)
        else:
            the_Category = get_object_or_404(Category, pk=pk)
            return Response(data=CategoryBlogSerializer(instance=the_Category).data, status=200)
    
    elif request.method == "POST":
        sb = CategoryBlogSerializer(data=request.data)
        if sb.is_valid():
            sb.save()
            return Response({'id': sb.instance.id}, status=201)
        else:
            return Response(sb.error_messages, status=406)
    elif request.method == 'PUT':
        the_Category = get_object_or_404(Category, pk=pk)
        sb = CategoryBlogSerializer(data=request.data, instance=the_Category)
        if sb.is_valid():
            sb.save()
            return Response('Updated', status=200)
        else:
            return Response(sb.error_messages, status=406)
    else:
        the_Category = get_object_or_404(Category, pk=pk)
        the_Category.delete()
        return Response('Deleted', status=200)


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryBlogSerializer


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryBlogSerializer


class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryBlogSerializer


class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryBlogSerializer



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Blog_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=BlogSerializer(instance=Blog.objects.all(), many=True).data, status=200)
        else:
            the_Blog = get_object_or_404(Blog, pk=pk)
            return Response(data=BlogSerializer(instance=the_Blog).data, status=200)
    
    elif request.method == "POST":
        sb = BlogSerializer(data=request.data)
        if sb.is_valid():
            sb.save()
            return Response({'id': sb.instance.id}, status=201)
        else:
            return Response(sb.error_messages, status=406)
    elif request.method == 'PUT':
        the_Blog = get_object_or_404(Blog, pk=pk)
        sb = BlogSerializer(data=request.data, instance=the_Blog)
        if sb.is_valid():
            sb.save()
            return Response('Updated', status=200)
        else:
            return Response(sb.error_messages, status=406)
    else:
        the_Blog = get_object_or_404(Blog, pk=pk)
        the_Blog.delete()
        return Response('Deleted', status=200)


class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogCreateAPIView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    parser_classes = (FormParser, MultiPartParser)


class BlogUpdateAPIView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDestroyAPIView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

