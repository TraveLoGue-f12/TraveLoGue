from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)

    def is_tourist(self):
        if self.status == 'T':
            return True
        return False

    def is_local(self):
        if self.status == 'L':
            return True
        return False
        
    def __str__(self):
        return self.user.username