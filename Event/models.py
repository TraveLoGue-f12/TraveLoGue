from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=700)
    place = models.CharField(max_length=255)
    # image = models.ImageField(null=True, blank=True, upload_to='images/')
    # imageURL = models.TextField(null = True)
    category = models.CharField(max_length=10, null=True, blank=True)
    # month = models.TextField(max_length=20, null=True, blank=True)

