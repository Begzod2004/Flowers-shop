from django.db import models





class Contact(models.Model):
    title = models.CharField(max_length=65)
    phone_number = models.CharField(max_length=12)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def str(self):
        return self.title
    

