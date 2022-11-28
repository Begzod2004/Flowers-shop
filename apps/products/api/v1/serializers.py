from rest_framework import serializers
from apps.products.models import *
from django.db.models import Avg , Sum, Count



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
        
class ProductFilterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = '__all__'
   
class SectionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sections
        fields = '__all__'
      
class SectionsCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SectionsCategory
        fields = '__all__'
     
class ProductReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductReview
        fields = '__all__'


class ProductReviewaSerializer(serializers.ModelSerializer):
    review_avg = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"


    def get_review_avg(self, obj):
        return ProductReview.objects.filter(product=obj).aggregate(Avg('star'), Sum('star'), Count('star'))

    
    
