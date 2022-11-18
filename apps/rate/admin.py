from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Rate)
class AutocarueAdmin(admin.ModelAdmin):
    list_display = ['title','description', 'date_create']
    list_filter = ['date_create']
    search_fields = ["title"]



