from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ObjekWisata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=20)
    address_link = models.URLField()