from django.test import TestCase

# Create your tests here.
from django.urls import *
from .views import *



urlpatterns = [
    path('category/', CategoryListAPIView.as_view()),
    path('category/create', CategoryCreateAPIView.as_view()),

    path('blog/create', BlogCreateAPIView.as_view()),
# coment
    path('comment/create', CommentCreateAPIView.as_view()),
    path('employee/create', EmployeeCreateAPIView.as_view()),
    path('employee', EmployeeListAPIView.as_view()),

]