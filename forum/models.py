from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    question = models.TextField()
    is_answered = models.BooleanField(default=False)

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    answer = models.TextField()