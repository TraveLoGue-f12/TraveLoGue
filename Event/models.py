from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to='images/')