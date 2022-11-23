from django.db import models
from apps.account.models import Account
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=65)
    image = models.ImageField(upload_to='blog/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(Account , on_delete=models.CASCADE, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title

class Employee(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='blog/')
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title

