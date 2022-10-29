from django.urls import path
from planner.views import *

app_name = 'planner'

urlpatterns = [
    path('', show_planner, name='planner'),
    path('json/', trips_json, name='trips_json'),
    path('addtrip/', addtrip_json, name='addtrip_json'),
]