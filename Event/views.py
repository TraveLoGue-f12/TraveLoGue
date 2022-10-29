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
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required(login_url='/login')
def show_event_detail(request, pk):
    data = Event.objects.get(id=pk)
    context = {
        'data' : data,
    }
    return render(request, "event_detail.html", context)


def show_event(request):
    data = Event.objects.all()
    user = request.user
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

@login_required(login_url='/login')
def show_event_json(request):
    event = Event.objects.all()
    return HttpResponse(serializers.serialize('json', event), content_type='application/json')

@login_required(login_url='/login')
def delete(request, pk):
    data = Event.objects.get(id=pk)
    data.delete()
    return HttpResponseRedirect(reverse('Event:show_event'))

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

@login_required(login_url='/login')
@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('description')
        place = request.POST.get('place')
        image = request.POST.get('image')
        event = Event.objects.create(title=title, date=date, place=place, description=description,image=image)

        result = {
            'fields': {
                'title' : event.title,
                'description' : event.description,
                'date' : event.date,
                'place': event.place,
                'image': event.image
            },
            'pk' : event.pk
        }

        return JsonResponse(result)