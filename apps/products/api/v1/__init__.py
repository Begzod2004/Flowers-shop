# from rest_framework import serializers
# from apps.products.models import *
# from django.db.models import Avg , Sum, Count
# from apps.account.api.v1.serializers import AccountSerializer

# class CategorySerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Category
#         fields = '__all__'


# class ProductSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Product
#         fields = '__all__'
        
# class ProductFilterSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Product
#         fields = '__all__'


# class GallerySerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Gallery
#         fields = '__all__'
   
# class SectionsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Sections
#         fields = '__all__'
      
# class SectionsCategorySerializer(serializers.ModelSerializer):

#     class Meta:
#         model = SectionsCategory
#         fields = '__all__'
     
# class ProductReviewSerializer(serializers.ModelSerializer):
#     user_id = AccountSerializer()

#     class Meta:
#         model = ProductReview
#         fields = '__all__'
        

   

# class ProductReviewaSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
#     review_avg = serializers.SerializerMethodField()

#     def to_representation(self, instance):
#         rep = super().to_representation(instance)
#         reviews = instance.productreview.all()
#         # rewiews = ProductReview.objects.filter(product = instance) # hanna oziga boglangan review larni olish
#         review_ser = ProductReviewSerializer(reviews, many=True)
#         rep["product_reviews"] = review_ser.data
#         return rep


#     class Meta:
#         model = Product
#         fields = "__all__"

#     def get_review_avg(self, obj):
#         return ProductReview.objects.filter(product=obj).aggregate(Avg('star'), Sum('star'), Count('star'))

    
    
