from django.db import models

# Create your models here.

class AboutCompany(models.Model):
    title = models.CharField(max_length=65)
    image = models.ImageField( upload_to='about_company/')
    description = models.TextField()

    def str(self):
        return self.title
