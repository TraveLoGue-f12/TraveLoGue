
from umkm.forms import UMKMForm
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from umkm.models import UMKM
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.db.models.fields.files import ImageFieldFile
from django.contrib.auth.decorators import login_required
from main.models import Profile
import json





def json_umkm(request):
    data = serializers.serialize('json', UMKM.objects.all())
    return HttpResponse(data, content_type="application/json")




def show_umkm_by_id(request, pk):
    data = UMKM.objects.get(id=pk)
    context = {
        'data' : data,
    }
    return render(request, "umkm_detail.html", context)

def show_umkm_by_user(request):
    userData = UMKM.objects.all()
    

    ctx = {
        'userDataList' : userData,
    }


    return render(request, "my_umkm.html", ctx)

# def show_umkm_by_user(request):
#     userData = UMKM.objects.filter(user=request.user)
    

#     ctx = {
#         'userDataList' : userData,
#     }


#     return render(request, "my_umkm.html", ctx)



@login_required(login_url='/login')
def show_data(request):
    getUser = Profile.objects.filter(user=request.user)
    

    for user in getUser:
        thisUser = user
        
   
    
    
    data_UMKM = UMKM.objects.all()

 
    
    
    response = {
        'datalist':  data_UMKM,
        'thisUser': thisUser,
 
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
        'thisUser': thisUser,
        }   
        return render(request, 'umkm_index.html', response)

    return render(request, "umkm_index.html", response)

@login_required(login_url='/login')
def delete_card(request, pk):
    UMKM.objects.get(id=pk).delete()
    return redirect('umkm:show_umkm_by_user')

@login_required(login_url='/login')
@csrf_exempt
def add_umkm_ajax(request):
    if request.method == 'POST':

        
      
        name = request.POST.get('name')
        description = request.POST.get('description')
        link_website = request.POST.get('link_website')
        
        
       
        umkm = UMKM.objects.create(user = request.user, name=name,  description=description, link_website=link_website)
       
        result = {
            
            'fields': {
                'user' : umkm.user,
                'name' : umkm.name,
                'description' : umkm.description,
                'link_website': umkm.link_website,
                
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
    
@csrf_exempt
def add_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        
        name = data["name"]
        description = data["description"]
        link_website = data["link_website"]
    
        addUMKM = UMKM.objects.create(
        name = name, 
        description = description,
        link_website = link_website
        )

        addUMKM.save()

      
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)