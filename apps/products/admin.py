from django.contrib import admin
from .models import Product,  ProductReview , Category, SectionsCategory, Gallery, Sections, Type_category,For_who


admin.site.register(Gallery)
admin.site.register(Sections)
admin.site.register(SectionsCategory)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductReview)
admin.site.register(For_who)
admin.site.register(Type_category)
