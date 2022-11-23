from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)

class BlogueAdmin(admin.ModelAdmin):
    list_display = ['title','is_active']
    list_filter = ['is_active']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','image','category','description','date_created','is_active']
    list_filter = ['date_created']
    search_fields = ["title"]

@admin.register(Comment)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog','description']
    search_fields = ["blog"]

@admin.register(Employee)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','description']
    search_fields = ["title"]