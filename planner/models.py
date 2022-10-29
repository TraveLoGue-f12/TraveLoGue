from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Trips(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    trip_date = models.CharField(max_length=10, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    notes = models.TextField(null=True)
    image = models.ImageField(null=True, blank=True)