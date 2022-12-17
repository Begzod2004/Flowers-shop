from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','created']
    list_filter = ['created']
    search_fields = ["id"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order','count']
    list_filter = ['order']
    search_fields = ["id"]
