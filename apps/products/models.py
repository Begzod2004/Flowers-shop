from django.db import models
from apps.account.models import Account

class Category(models.Model):
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Parent category", limit_choices_to={'is_active': True, 'parent_category__isnull': True}, related_name='children', null=True, blank=True)
    title = models.CharField(max_length=50, verbose_name="Category title")
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class For_who(models.Model):
    title = models.CharField(max_length=50, verbose_name="Kim uchun")
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title


class Type_category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Turining nomi")
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title



class Product(models.Model):
    title = models.CharField(max_length=254,verbose_name="Nomi")
    color = models.CharField(max_length=20, null=True,blank=True,verbose_name="Rangi")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Category")
    for_who = models.ForeignKey('For_who', on_delete=models.CASCADE, verbose_name="Kim uchun")
    type_category = models.ForeignKey('Type_category', on_delete=models.CASCADE, verbose_name="Turi categoriysi")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    product_image1 = models.ImageField(null=False, blank=True,verbose_name="Birinchi rasm")
    product_image2= models.ImageField(null=False, blank=True,verbose_name="Ikkinchi rasm")
    product_image3= models.ImageField(null=False, blank=True,verbose_name="Uchinchi rasm")
    product_image4= models.ImageField(null=False, blank=True,verbose_name="Tortinchi rasm")
    length = models.CharField(max_length=30, verbose_name="uzunligi") #uzunligi
    width = models.CharField(max_length=40,verbose_name="eni") #eni
    count = models.CharField(max_length=50,verbose_name="Nechtaligi") #nechtaligi

    def __str__(self):
        return self.title


class ProductReview(models.Model):
    user_id = models.ForeignKey(Account, null=True, blank=True, on_delete=models.SET_NULL)
    star = models.IntegerField(default=0 , verbose_name = "star")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True, verbose_name='review_created_date')
    
   

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



    




