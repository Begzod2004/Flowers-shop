from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Cart)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','created']
    list_filter = ['created']
    search_fields = ["id"]

@admin.register(Cartitems)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['cart','product','quantity',]
    search_fields = ["cart", "product"]
    list_filter = ['product']