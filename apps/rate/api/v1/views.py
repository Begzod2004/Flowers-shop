from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import json
from apps.autopark.models import Category, Rate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *
from rest_framework.parsers import FormParser, MultiPartParser
# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Rate_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=RateSerializer(instance=Rate.objects.all(), many=True).data, status=200)
        else:
            the_Rate = get_object_or_404(Rate, pk=pk)
            return Response(data=RateSerializer(instance=the_Rate).data, status=200)
  
class RateListAPIView(ListAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class RateCreateAPIView(CreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    parser_classes = (FormParser, MultiPartParser)


class RateUpdateAPIView(UpdateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class RateDestroyAPIView(DestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

