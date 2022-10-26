from django.db import models

# Create your models here.
class UMKM(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    link_website = models.URLField()
    image = models.ImageField(null = True, blank =True,upload_to='images/')  