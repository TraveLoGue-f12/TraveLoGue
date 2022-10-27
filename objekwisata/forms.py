from django.db import models  
from django.forms import ModelForm, fields  
from .models import ObjekWisata
from django import forms  

class ObjekWisataForm(ModelForm):
    class Meta:
        model = ObjekWisata
        fields = ('image', 'title', 'description', 'alamat')