from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UMKM(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    link_website = models.URLField()
    