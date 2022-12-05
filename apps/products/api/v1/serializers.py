from rest_framework import serializers
from apps.products.models import *
from django.db.models import Avg , Sum, Count



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        


class For_whoSerializer(serializers.ModelSerializer):

    class Meta:
        model = For_who
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


    
class LengthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Length
        fields = "__all__"

     
    
class CountCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CountCategory
        fields = "__all__"
    
class WidthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Width
        fields = "__all__"

class ProductReviewaSerializer(serializers.ModelSerializer):
    countCategory = CountCategorySerializer()
    width = WidthSerializer()
    length = LengthSerializer()
    for_who = For_whoSerializer()
    category = CategorySerializer()
    review_avg = serializers.SerializerMethodField()

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        reviews = instance.productreview.all()
        # rewiews = ProductReview.objects.filter(product = instance) # hamma oziga boglangan review larni olish
        review_ser = ProductReviewSerializer(reviews, many=True)
        rep["product_reviews"] = review_ser.data
        return rep

    class Meta:
        model = Product
        fields = "__all__"

    def get_review_avg(self, obj):
        return ProductReview.objects.filter(product=obj).aggregate(Avg('star'), Sum('star'), Count('star'))




