from django.db import models
from apps.account.models import Account
from apps.autopark.models import Car



class Weight_cargo(models.Model):
    title = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Volume_cargo(models.Model):
    title = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Type_cargo(models.Model):
    title = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Mode_cargo(models.Model):
    title = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(Account ,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    title = models.CharField(max_length=65)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    from_here = models.CharField(max_length=50) 
    to_here = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    weight_cargo = models.ForeignKey(Weight_cargo,on_delete=models.CASCADE)
    volume_cargo = models.ForeignKey(Volume_cargo ,on_delete=models.CASCADE)
    type_cargo = models.ForeignKey(Type_cargo,on_delete=models.CASCADE)
    mode_cargo = models.ForeignKey(Mode_cargo ,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="apps/order/", null=True)
    image2 = models.ImageField(upload_to="apps/order/", null=True, blank=True)
    image3 = models.ImageField(upload_to="apps/order/", null=True,  blank=True)
    def __str__(self):
         return f"{self.title} {self.image}"

