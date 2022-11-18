from rest_framework.response import Response 
from django.shortcuts import get_object_or_404, render
from apps.contact.models import Contact
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import *
from django.http import JsonResponse
# Create your views here.

def test_api_view(request):
    first_Contact = Contact.objects.first()
    f_b = {
        'title': first_Contact.title,
        'is_active': first_Contact.status,
        'is_active': first_Contact.phone_number,
        'is_active': first_Contact.date_created,
    }
    return JsonResponse(f_b)
