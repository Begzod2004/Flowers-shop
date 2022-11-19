from django.urls import path
from .views import *


urlpatterns = [
    # products
    path('product_api_view/', ProductListAPIView.as_view()),
    path('product_api_view/create', ProductCreateAPIView.as_view()),
    path('product_api_view/<int:pk>/', Product_api_view),

    # Images
    path('image_api_view/', ImageListAPIView.as_view()),
    path('image_api_view/create', ImageCreateAPIView.as_view()),
    path('image_api_view/<int:pk>/', Image_api_view),
    
    # Colors
    path('color_api_view/', ColorListAPIView.as_view()),
    path('color_api_view/create', ColorCreateAPIView.as_view()),
    path('color_api_view/<int:pk>/', Color_api_view),
    
    # Flowers
    path('flower_api_view/', FlowerListAPIView.as_view()),
    path('flower_api_view/create', FlowerCreateAPIView.as_view()),
    path('flower_api_view/<int:pk>/', Flower_api_view),
    
    # ProductReview
    path('productReview_api_view/', ProductReviewListAPIView.as_view()),
    path('productReview_api_view/create', ProductReviewCreateAPIView.as_view()),
    path('productReview_api_view/<int:pk>/', ProductReview_api_view),
    ]