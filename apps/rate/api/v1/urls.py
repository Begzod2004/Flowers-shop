from django.test import TestCase

# Create your tests here.
from django.urls import *
from .views import *



urlpatterns = [
    path('Rate-api-view/', RateListAPIView.as_view()),
    path('Rate-api-view/create', RateCreateAPIView.as_view()),
    path('Rate-api-view/update/<int:pk>', RateUpdateAPIView.as_view()),
    path('Rate-api-view/delete/<int:pk>', RateDestroyAPIView.as_view()),    
]