from rest_framework import serializers
from apps.blog.models import Category, Blog



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'
        


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'

        
class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'

        
class FlowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'

        
class ProductReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'
