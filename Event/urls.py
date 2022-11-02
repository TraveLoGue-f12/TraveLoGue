from django.urls import path
from Event.views import show_event_json
from Event.views import show_event
from Event.views import show_event_detail
from Event.views import membuat_event
from Event.views import add_event
from Event.views import delete
from Event.views import show_user_event
from Event.views import show_music_event
from Event.views import edit_event
from Event.views import show_sport_event
from Event.views import show_culinary_event
from Event.views import show_festival_event
from Event.views import show_culture_event
from Event.views import show_others_event

app_name = 'Event'

urlpatterns = [
    path('', show_event, name='show_event'),
    path('json/', show_event_json, name='show_event_json'),
    path('add/', membuat_event, name='membuat_event'),
    path('add-new/', add_event, name='add_event'),
    path('delete/<int:pk>', delete, name='delete'),
    path('my-event/delete/<int:pk>', delete, name='delete'),
    path('event-detail/<int:pk>', show_event_detail, name='show_event_detail'),
    path('music/event-detail/<int:pk>', show_event_detail, name='show_event_detail'),
    path('sport/event-detail/<int:pk>', show_event_detail, name='show_event_detail'),
    path('festival/event-detail/<int:pk>', show_event_detail, name='show_event_detail'),
    path('culinary/event-detail/<int:pk>', show_event_detail, name='show_event_detail'),
    path('culture/event-detail/<int:pk>', show_event_detail, name='show_event_detail'),
    path('others/event-detail/<int:pk>', show_event_detail, name='show_event_detail'),
    path('my-event/', show_user_event, name='show_user_event'),
    path('my-event/edit-event/<int:pk>', edit_event, name='edit_event'),
    path('music/', show_music_event, name='show_music_event'),
    path('sport/', show_sport_event, name='show_sport_event'),
    path('culinary/', show_culinary_event, name='show_culinary_event'),
    path('festival/', show_festival_event, name='show_festival_event'),
    path('culture/', show_culture_event, name='show_culture_event'),
    path('others/', show_others_event, name='show_others_event'),
]