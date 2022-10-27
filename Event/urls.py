from django.urls import path
from Event.views import show_event_json
from Event.views import show_event
from Event.views import show_event_detail
from Event.views import membuat_event
from Event.views import delete

app_name = 'Event'

urlpatterns = [
    path('', show_event, name='show_event'),
    path('json/', show_event_json, name='show_event_json'),
    path('add/', membuat_event, name='membuat_event'),
    path('delete/<int:pk>', delete, name='delete'),
    path('event-detail/<int:pk>', show_event_detail, name='show_event_detail'),
]