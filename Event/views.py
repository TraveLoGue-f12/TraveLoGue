from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Profile
from django.contrib.auth import authenticate, login, logout
from Event.forms import EventForm
from Event.models import Event
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.urls import reverse
from main.models import Profile, User
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models.fields.files import ImageFieldFile
import json

# Create your views here.

@login_required(login_url='/login')
def show_event_detail(request, pk):
    data = Event.objects.get(id=pk)
    context = {
        'data' : data,
    }
    return render(request, "event_detail.html", context)

@login_required(login_url='/login')
def show_music_event(request):
    data = Event.objects.filter(category="Music")
    # get_month = data.date
    # bulan = get_month[3:5]
    context = {
        # 'bulan': bulan,
        'data' : data,
    }
    return render(request, "music.html", context)

@login_required(login_url='/login')
def show_sport_event(request):
    data = Event.objects.filter(category="Sport")
    context = {
        'data' : data,
    }
    return render(request, "sport.html", context)

@login_required(login_url='/login')
def show_culinary_event(request):
    data = Event.objects.filter(category="Culinary")
    context = {
        'data' : data,
    }
    return render(request, "culinary.html", context)

@login_required(login_url='/login')
def show_festival_event(request):
    data = Event.objects.filter(category="Festival")
    context = {
        'data' : data,
    }
    return render(request, "festival.html", context)

@login_required(login_url='/login')
def show_culture_event(request):
    data = Event.objects.filter(category="Culture")
    context = {
        'data' : data,
    }
    return render(request, "culture.html", context)

@login_required(login_url='/login')
def show_others_event(request):
    data = Event.objects.filter(category="Others")
    context = {
        'data' : data,
    }
    return render(request, "others.html", context)

@login_required(login_url='/login')
def show_user_event(request):
    user = request.user
    if user.is_authenticated:
        user_profile = Profile.objects.get(user=user)
        context = {
            "data" : Event.objects.filter(user=user)
        }
        return render(request, 'userevent.html', context)

@login_required(login_url='/login')
def show_event(request):
    data = Event.objects.all()
    user = request.user

    # for datadetail in data:
    #     if datadetail.image != "":
    #         if isinstance(datadetail.image, ImageFieldFile):
                
    #             datadetail.imageURL = str(datadetail.image.url)

    #         datadetail.save()

    context = {
        'event_data' : data,
    }
    if user.is_authenticated:
        user_profile = Profile.objects.get(user=user)
        context = {
            'event_data' : data,
            'status' : user_profile.full_name
        }

        if user_profile.status == 'L':
            if request.method == 'POST':
                form = EventForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(reverse('Event:show_event'))
            else:
                form = EventForm()
                response = {
                'status': user_profile.full_name,
                'event_data': data,
                'form': form,
                'detector': "yes",
                }   
                return render(request, 'event.html', response)

    return render(request, "event.html", context)

# @login_required(login_url='/login')
def show_event_json(request):
    event = Event.objects.all()
    return HttpResponse(serializers.serialize('json', event), content_type='application/json')

def show_userevent_json(request):
    event = Event.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', event), content_type='application/json')

def show_music_json(request):
    event = Event.objects.filter(category="Music")
    return HttpResponse(serializers.serialize('json', event), content_type='application/json')

def show_festival_json(request):
    event = Event.objects.filter(category="Festival")
    return HttpResponse(serializers.serialize('json', event), content_type='application/json')

def show_culinary_json(request):
    event = Event.objects.filter(category="Culinary")
    return HttpResponse(serializers.serialize('json', event), content_type='application/json')

def show_sport_json(request):
    event = Event.objects.filter(category="Sport")
    return HttpResponse(serializers.serialize('json', event), content_type='application/json')

def show_culture_json(request):
    event = Event.objects.filter(category="Culture")
    return HttpResponse(serializers.serialize('json', event), content_type='application/json')

def show_others_json(request):
    event = Event.objects.filter(category="Others")
    return HttpResponse(serializers.serialize('json', event), content_type='application/json')

@login_required(login_url='/login')
def delete(request, pk):
    data = Event.objects.get(id=pk)
    data.delete()
    return HttpResponseRedirect(reverse('Event:show_user_event'))

def membuat_event(request):
    if request.method == 'POST':
        form_event = EventForm(request.POST, request.FILES)
        if form_event.is_valid():
            form_event.save()
            response = HttpResponseRedirect(reverse("Event:show_event")) 
            return response
    else:
        form_event = EventForm()
        return render(request, "add_event.html", {"form": form_event})

def edit_event(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)
    
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Event:show_user_event'))
    
    context = {'form':form}
    return render(request, 'editevent.html', context)

@login_required(login_url='/login')
@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        place = request.POST.get('place')
        # image = request.FILES.get('image')
        category = request.POST.get('category')
        event = Event.objects.create(user=request.user, title=title, date=date, place=place, description=description, category=category)


        result = {
            'fields': {
                'title' : event.title,
                'description' : event.description,
                'date' : event.date,
                'place': event.place,
                # 'image': str(event.image),
                'category': event.category,

            },
            'pk' : event.pk
        }

        return JsonResponse(result)

@csrf_exempt
def add_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        
        title = data["title"]
        description = data["description"]
        date = data["date"]
        place = data["place"]
        category = data["category"]

        add_event = Event.objects.create(
            user = request.user, 
            date = date,
            title = title,
            place = place,
            description = description,
            category = category
        )

        add_event.save()
    
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def delete_flutter(request):
    data = json.loads(request.body)
    pk = int(data["pk"])
    
    Event.objects.get(id=pk).delete()
    return JsonResponse({"status": "success"}, status=200)

def flutter_json(request, username):
    user = User.objects.get(username = username)
    if user is not None:
        data = Event.objects.filter(user=user)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    else:
        return JsonResponse({}, status=404)

@csrf_exempt
def edit_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        pk = int(data["pk"])
        event = Event.objects.get(id=pk)
        
        event.category = data["category"]
        event.title = data["title"]
        event.place = data["place"]
        event.date = data["date"]
        # event.start_date = datetime.strptime(data["start_date"], "%Y-%m-%d")
        # event.end_date = datetime.strptime(data["end_date"], "%Y-%m-%d")
        event.description = data["description"]

        event.save()
         
        return JsonResponse({"status": "success"}, status=200)

    else:
        return JsonResponse({"status": "error"}, status=401)
    # print("a")
    # data = json.loads(request.body)
    # print()
    # print(data)
    # title = data["title"]
    # description = data["description"]
    # date = data["date"]
    # place = data["place"]
    # category = data["category"]
    
    # Event.objects.get(
    #         date = date,
    #         title = title,
    #         place = place,
    #         description = description,
    #         category = category).delete()
    # return JsonResponse({"status": "success"}, status=200)

# def add_flutter(request):
#     if request.method == 'POST':
        
#         data = json.loads(request.body)
        
#         title = data["title"]
#         description = data["description"]
#         date = data["date"]
#         place = data["place"]
#         category = data["category"]

#         try:
#             Event.objects.get(title=title, description=description, date=date, place=place, category=category)
#             return JsonResponse({"status": "dup"}, status=401)
#         except:
#             addEvent = Event.objects.create(
#             title=title,
#             description=description,
#             date=date,
#             place=place,
#             category=category
#             )

#             addEvent.save()

        
#             return JsonResponse({"status": "success"}, status=200)
#     else:
#         return JsonResponse({"status": "error"}, status=401)
