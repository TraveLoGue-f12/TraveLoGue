from django.shortcuts import render

from objekwisata.models import ObjekWisata
from django.core import serializers
from django.http.response import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request, 'objekwisata.html')

def show_objekwisata(request):
    objekwisata = ObjekWisata.objects.all()
    return HttpResponse(serializers.serialize('json', objekwisata), content_type='application/json')