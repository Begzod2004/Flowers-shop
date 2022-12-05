from django.urls import path
from .views import *


# this order urls
urlpatterns = [
    path('order', OrderListAPIView.as_view()),
    path('orderITEM', OrderItemListAPIView.as_view()),
    path('order/create', OrderCreateAPIView.as_view()),
    path('orderITEM/create', OrderItemCreateAPIView.as_view()),
    path('order/<int:pk>/', Order_api_view)
]