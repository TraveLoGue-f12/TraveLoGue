from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ObjekWisata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.TextField()
    description = models.TextField()
    location = models.TextField()
    address_link = models.URLField()