from django import forms
from django.forms import ModelForm, widgets
from planner.models import Trips

class updateTripForm(ModelForm):
    name = forms.CharField(required=False)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    notes = forms.CharField(widget = forms.Textarea, required=False)

    class Meta:
        model = Trips
        fields = ['name', 'start_date', 'end_date', 'notes']