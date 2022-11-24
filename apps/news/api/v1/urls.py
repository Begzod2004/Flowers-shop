from django.urls import path
from .views import NewsCreateAPIView, NewsListAPIView, News_api_view



urlpatterns = [
    path('news', NewsListAPIView.as_view()),
    path('news/create', NewsCreateAPIView.as_view()),

    path('news/<int:pk>/', News_api_view)
]