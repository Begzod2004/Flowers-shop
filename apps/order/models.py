from django.db import models
from apps.products.models import Product
from apps.account.models import Account

import uuid


CONTACT_STATUS = (
    (0,"New"),
    (1,"Prosess"),
    (2,"Canceled"),
    (3,"Finished")
)




class Order(models.Model):
    user_id = models.ForeignKey(Account,on_delete=models.CASCADE)
    product_number = models.UUIDField(primary_key=True, default=str(uuid.uuid4().int)[:6], editable=False,unique=True)
    status = models.IntegerField(choices=CONTACT_STATUS, default=0)
    product = models.ManyToManyField(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='cartitems')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)












   