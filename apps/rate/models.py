from django.db import models



class Rate(models.Model):
    title = models.CharField(max_length=65)
    image = models.ImageField(upload_to='rate/')
    description = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title


