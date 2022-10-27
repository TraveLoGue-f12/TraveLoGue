from django.shortcuts import render
from umkm.forms import UMKMForm
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from umkm.models import UMKM
from django.shortcuts import redirect


def index(request):
    return render(request, 'umkm_index.html')

def add_umkm(request):
    if request.method == 'POST':
        form = UMKMForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('umkm:rekomendasi_umkm'))
    else:
        form = UMKMForm()
        response = {'form': form}
        return render(request, 'add_umkm.html', response)

def json_umkm(request):
    data = serializers.serialize('json', UMKM.objects.all())
    return HttpResponse(data, content_type="application/json")

def show_data(req):
    
    data_UMKM = UMKM.objects.all()
  
    ctx = {
        'datalist':  data_UMKM,
    }

    return render(req, "umkm_index.html", ctx)

def delete_card(request, pk):
    UMKM.objects.get(id=pk).delete()
    return redirect('umkm:rekomendasi_umkm')
    