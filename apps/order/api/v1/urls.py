from django.urls import path
from .views import OrderCreateAPIView, OrderListAPIView, Order_api_view


# this order urls
urlpatterns = [
    path('order', OrderListAPIView.as_view()),
    path('order/create', OrderCreateAPIView.as_view()),
    path('order/<int:pk>/', Order_api_view)
]