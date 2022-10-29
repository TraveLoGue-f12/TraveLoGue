from django import forms
from django.db.models import fields
from .models import Event
# from django.forms import widgets

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'place', 'image']