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

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'
        
class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = '__all__'
   
class FlowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flower
        fields = '__all__'
     
class ProductReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductReview
        fields = '__all__'

# class CreateRatingSerializer(serializers.ModelSerializer):
#     """Добавление рейтинга пользователем"""
#     class Meta:
#         model = ProductReview
#         fields = ("product_id", "user_id", "rating_score", "review_title", "review_comment", "review_date")

#     def create(self, validated_data):
#         rating, _ = ProductReview.objects.update_or_create(
#             product_id=validated_data.get('product_id', None),
#             user_id=validated_data.get('user_id', None),
#             rating_score=validated_data.get('rating_score', None),
#             review_title=validated_data.get('review_title', None),
#             review_comment=validated_data.get('review_comment', None),
#             review_date=validated_data.get('review_date', None),
#             defaults={'rating_score': validated_data.get("rating_score")}
#         )
#         return rating

class ProductReviewaSerializer(serializers.ModelSerializer):
    # image = serializers.SerializerMethodField()
    # color = serializers.SerializerMethodField()
    review_avg = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"


    def get_review_avg(self, obj):
        return ProductReview.objects.filter(product=obj).aggregate(Avg('star'), Sum('star'), Count('star'))

    