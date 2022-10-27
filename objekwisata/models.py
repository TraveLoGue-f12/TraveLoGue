from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class ObjekWisata(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    lokasi = models.CharField(max_length=250, default="Indonesia")
    title = models.CharField(max_length=25)
    deskripsi = models.CharField(max_length=50)
    alamat = models.URLField()