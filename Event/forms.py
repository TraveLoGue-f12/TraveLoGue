from django import forms
from django.db.models import fields
from .models import Event
# from django.forms import widgets

class EventForm(forms.ModelForm):
    STATUS_CHOICES = [('Music', 'Music'), ('Sport', 'Sport'), ('Festival', 'Festival'), ('Culinary', 'Culinary'), ('Culture', 'Culture'), ('Others', 'Others')]
    category = forms.ChoiceField(
        label="Event Category",
        required=True,
        choices=STATUS_CHOICES
    )

    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'place', 'category']