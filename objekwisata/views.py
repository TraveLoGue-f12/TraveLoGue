from django.shortcuts import render
from objekwisata.forms import ObjekWisataForm
from objekwisata.models import ObjekWisata
from django.core import serializers
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.db.models.fields.files import ImageFieldFile
from main.models import Profile


# Create your views here.
@login_required(login_url='/login')
def index(request):
    data_objekwisata = ObjekWisata.objects.all()

    response = {
        'data':  data_objekwisata,
        'user_status': '',
        'user_loggedin': request.user.username,
    }  

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        response['user_status'] = profile.status
    
    if request.method == 'POST':
        form = ObjekWisataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect(reverse('objekwisata:objekwisata'))
    else:
        form = ObjekWisataForm()
        response = {
            'data':  data_objekwisata,
            'form': form,
            'user_status' : '',
        }  

        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            response['user_status'] = profile.status
  
        return render(request, 'objekwisata.html', response)

    return render(request, "objekwisata.html", response)

def show_objekwisata_json(request):
    objekwisata = ObjekWisata.objects.all()
    return HttpResponse(serializers.serialize('json', objekwisata), content_type='application/json')

@login_required(login_url='/login')
@csrf_exempt
def add_objekwisata_ajax(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        address_link = request.POST.get('address_link')

        objekwisata = ObjekWisata.objects.create(title=title, description=description, location=location, address_link=address_link)

        result = {
            'fields': {
                'title': objekwisata.title,
                'description': objekwisata.description,
                'location': objekwisata.location,
                'address_link': objekwisata.address_link,
            },
            'pk': objekwisata.pk
        }
        return JsonResponse(result)
