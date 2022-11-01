from datetime import datetime
from django.shortcuts import render, redirect
from main.models import Profile
from planner.forms import updateTripForm
from planner.models import Trips
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/login')
def show_planner(request):
    user = request.user
    if user.is_authenticated:
        user_profile = Profile.objects.get(user=user)
        context = {
            "full_name" : user_profile.full_name,
            "plans" : Trips.objects.filter(user=user)
        }
        return render(request, 'planner.html', context)


def trips_json(request):
    data = Trips.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def delete_trip(request, pk):
    Trips.objects.get(id=pk).delete()
    return redirect('planner:planner')

def update_trip(request, pk):
    trip = Trips.objects.get(id=pk)
    form = updateTripForm(instance=trip)
    print(333)
    
    if request.method == "POST":
        print(222)
        form = updateTripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            print(111)
            return redirect('planner:planner')
    
    context = {'form':form}
    return render(request, 'edit-plan.html', context)

@csrf_exempt
def addtrip_json(request):
    if request.method == 'POST':
        image = request.POST.get('image')
        name = request.POST.get('name')
        trip_date = request.POST.get('tripDate')
        start_date = datetime.strptime(trip_date.split(' - ')[0], "%d/%m/%Y")
        end_date = datetime.strptime(trip_date.split(' - ')[1], '%d/%m/%Y')
        notes = request.POST.get('tripNotes')

        trip = Trips.objects.create(
            user = request.user,
            image = image,
            name = name,
            trip_date = trip_date,
            start_date = start_date,
            end_date = end_date,
            notes = notes,
            )

        result = {
            'pk':trip.pk,
            'fields':{
                'image':str(trip.image),
                'name':trip.name,
                'trip_date':trip.trip_date,
                'start_date':trip.start_date,
                'end_date':trip.end_date,
                'notes':trip.notes,
            }
        }

        return JsonResponse(result)


