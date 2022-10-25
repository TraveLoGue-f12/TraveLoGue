from django.db.models import fields
from umkm.models import UMKM
from django.forms import ModelForm

class UMKMForm(ModelForm):
    class Meta:
        model = UMKM
        fields = '__all__'
