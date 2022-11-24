from django.db import models
from apps.account.models import Account

class Category(models.Model):
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Parent category", limit_choices_to={'is_active': True, 'parent_category__isnull': True}, related_name='children', null=True, blank=True)
    title = models.CharField(max_length=50, verbose_name="Category title")
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=254)
    color = models.CharField(max_length=20, null=True,blank=True )
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Category")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    product_image = models.ImageField(null=False, blank=True)

    def __str__(self):
        return self.title



class Image(models.Model):
    name = models.CharField(max_length=254, null=False, blank=True)
    image = models.ImageField(upload_to="fowerImg/", null=False, blank=False)
    URL = models.URLField(max_length=1024, null=False, blank=True)
    product = models.ForeignKey('Product', null=True,
                                   blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{}, {}'.format(self.name, self.product_id)




class ProductReview(models.Model):
    user_id = models.ForeignKey(Account, null=True, blank=True, on_delete=models.SET_NULL)
    star = models.IntegerField(default=0 , verbose_name = "star")
    review_date = models.DateTimeField(auto_now_add=True, verbose_name='review_created_date')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_comment = models.TextField()
    
   

    def __str__(self):
        return format(self.user_id)

class Gallery(models.Model):
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return format(self.image)


class SectionsCategory(models.Model):
    title = models.CharField(max_length=30)
    
    def __str__(self):
        return format(self.title)


class Sections(models.Model):
    title = models.CharField(max_length=30,null=False, blank=False)
    category = models.ForeignKey(SectionsCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="CarsImages", null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return format(self.title)


    




