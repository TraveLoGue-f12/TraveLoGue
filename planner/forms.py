from django import forms
from django.forms import ModelForm
from planner.models import Trips
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Div

class updateTripForm(ModelForm):
    name = forms.CharField(required=False)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    notes = forms.CharField(widget = forms.Textarea, required=False)

    class Meta:
        model = Trips
        fields = ['name', 'start_date', 'end_date', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row('name'),
            Row(
                Column('start_date', css_class='col-md-6 col-lg-6 p-0'),
                Column('end_date', css_class='col-md-6 col-lg-6 p-0'),
                css_class='d-flex justify-content-between'
            ),
            Row(Column('notes'))
        )
