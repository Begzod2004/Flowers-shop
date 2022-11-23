from rest_framework import serializers
from apps.blog.models import Category, Blog , Comment, Employee


class CategoryBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields ='__all__'

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
