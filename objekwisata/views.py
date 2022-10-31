from django.shortcuts import render
from objekwisata.forms import ObjekWisataForm
from objekwisata.models import ObjekWisata
from django.core import serializers
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'objekwisata.html')

# def add_objekwisata(request):
#     data_objekwisata = ObjekWisata.objects.all()
#     response = {
#         'datalist':  data_objekwisata,
#     }  
    
#     if request.method == 'POST':
#         form = ObjekWisataForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('objekwisata:rekomendasi_objekwisata'))
#     else:
#         form = ObjekWisataForm()
#         response = {
#             'datalist':  data_objekwisata,
#             'form': form,
#         }   
#         return render(request, 'objekwisata.html', response)

#     return render(request, "objekwisata.html", response)

def show_objekwisata_json(request):
    objekwisata = ObjekWisata.objects.all()
    return HttpResponse(serializers.serialize('json', objekwisata), content_type='application/json')

@csrf_exempt
@login_required(login_url='/login')
def add_objekwisata(request):
    if request.method == 'POST':
        title = request.POST.get('name')
        description = request.POST.get('description')
        address_link = request.POST.get('address_link')
        image = request.POST.get('image')

        objekwisata = objekwisata.objects.create(title=title, description=description, address=address_link, image=image)

        result = {
            'fields': {
                'title' : objekwisata.title,
                'description' : objekwisata.description,
                'address' : objekwisata.address_link,
                'image': objekwisata.image,
            },
            'pk' : objekwisata.pk
        }
        return JsonResponse(result)