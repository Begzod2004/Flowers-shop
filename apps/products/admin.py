from django.contrib import admin
from .models import Product, Image, ProductReview , Category, SectionsCategory, Gallery, Sections


admin.site.register(Gallery)
admin.site.register(Sections)
admin.site.register(SectionsCategory)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(ProductReview)
