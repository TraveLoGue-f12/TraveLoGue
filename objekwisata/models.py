from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class ObjekWisata(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100, default=" ")
    address_link = models.URLField(default="https://goo.gl/maps/5D8wXfWReu4EhZNB6")
    image = models.ImageField(null=True, blank=True, upload_to='images/')