from django.db import models


class New(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to="newsImg/", null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)    
    
    def __str__(self):
        return self.title