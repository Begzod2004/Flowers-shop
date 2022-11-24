from django.contrib import admin
from .models import Product, Image, ProductReview , Category


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(ProductReview)
