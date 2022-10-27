from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Event.forms import EventForm
from Event.models import Event
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def show_event(request):
    data = Event.objects.all()
    context = {
        'event_data' : data,
    }
    return render(request, "event.html", context)

def show_event_json(request):
    event = Event.objects.all()
    return HttpResponse(serializers.serialize('json', event), content_type='application/json')

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

def add_event(request):
    form_event = EventForm(request.POST or None)
    if request.method == "POST" and form_event.is_valid():
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('description')
        place = request.POST.get('place')
        event = Event.objects.create(title=title, date=date, place=place, description=description,user=request.user)

        result = {
            'fields': {
                'title' : event.title,
                'description' : event.description,
                'date' : event.date,
            },
            'pk' : event.pk
        }
    
    return JsonResponse(result)

