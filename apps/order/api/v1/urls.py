from django.urls import path
from .views import CartCreateAPIView, CartListAPIView, Cart_api_view


# this order urls
urlpatterns = [
    path('cart', CartListAPIView.as_view()),
    path('cart/create', CartCreateAPIView.as_view()),
    path('cart/<int:pk>/', Cart_api_view)
]