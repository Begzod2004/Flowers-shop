from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user_id','created']
    list_filter = ['created']
    search_fields = ["id"]
