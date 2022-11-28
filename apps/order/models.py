from django.db import models
from apps.products.models import Product
from apps.account.models import Account
import uuid
import random

def random_string():
    return str(random.randint(10000, 999999))
    
CONTACT_STATUS = (
    (0,"New"),
    (1,"Prosess"),
    (2,"Canceled"),
    (3,"Finished")
)

class Order(models.Model):
    product_num = models.CharField(max_length=1000,default = random_string)    
    user_id = models.ForeignKey(Account,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    status = models.IntegerField(choices=CONTACT_STATUS, default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)












   