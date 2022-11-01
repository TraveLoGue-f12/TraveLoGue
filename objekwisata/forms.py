from django.forms import ModelForm
from objekwisata.models import ObjekWisata

class ObjekWisataForm(ModelForm):
    class Meta:
        model = ObjekWisata
        fields = ["title", "description", "location", "address_link", "image"]