from django.urls import path
from planner.views import *

app_name = 'planner'

urlpatterns = [
    path('', show_planner, name='planner'),
    path('json/', trips_json, name='trips_json'),
    path('addtrip/', addtrip_json, name='addtrip_json'),
    path('delete/<int:pk>/', delete_trip, name='delete_trip'),
    path('change/<int:pk>/', update_trip, name="update_trip"),
    path('addflutter/', addtrip_flutter, name="addtrip_flutter"),
    path('deleteflutter/', delete_flutter, name='delete_flutter'),
    path('editflutter/', edit_flutter, name='edit_flutter'),
    path('jsonflutter/<str:username>', flutter_json, name='flutter_json'),
]