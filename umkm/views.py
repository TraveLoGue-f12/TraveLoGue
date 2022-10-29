
from umkm.forms import UMKMForm
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from umkm.models import UMKM
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt


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

def show_umkm_by_id(request, pk):
    data = UMKM.objects.get(id=pk)
    context = {
        'data' : data,
    }
    return render(request, "umkm_detail.html", context)

def show_data(request):
  
    data_UMKM = UMKM.objects.all()
    response = {
        'datalist':  data_UMKM,
 
    }  
    
    if request.method == 'POST':
        form = UMKMForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('umkm:rekomendasi_umkm'))
    else:
        form = UMKMForm()
        response = {
        'datalist':  data_UMKM,
        'form': form,
        }   
        return render(request, 'umkm_index.html', response)

    return render(request, "umkm_index.html", response)

def delete_card(request, pk):
    UMKM.objects.get(id=pk).delete()
    return redirect('umkm:rekomendasi_umkm')
    
@csrf_exempt
def add_umkm_ajax(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        link_website = request.POST.get('link_website')
        
        image = request.POST.get('image')
        umkm = UMKM.objects.create(name=name,  description=description,image=image, link_website=link_website)

        result = {
            'fields': {
                'name' : umkm.name,
                'description' : umkm.description,
                'link_website': umkm.link_website,
                'image': umkm.image
            },
            'pk' : umkm.pk
        }

        return JsonResponse(result)

@csrf_exempt
def delete_umkm_ajax(request, id):
    if request.method == "DELETE":
        umkm = get_object_or_404(UMKM, id = id)
        umkm.delete()
    return HttpResponse(status=202)
    