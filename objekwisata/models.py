from django.db import models

# Create your models here.
class ObjekWisata(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=20)
    address_link = models.URLField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    imageURL = models.TextField(null=True) 