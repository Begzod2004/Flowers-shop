from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
import json
from apps.contact.models import Contact
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import *
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Contact_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=ContactSerializer(instance=Contact.objects.all(), many=True).data, status=200)
        else:
            the_Contact = get_object_or_404(Contact, pk=pk)
            return Response(data=ContactSerializer(instance=the_Contact).data, status=200)
    

class ContactListAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
