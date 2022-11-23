from django.contrib import admin
from .models import Product, Image, Color, Flower, ProductReview , Category


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Color)
admin.site.register(Flower)
admin.site.register(ProductReview)
