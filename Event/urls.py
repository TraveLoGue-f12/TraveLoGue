from django.urls import path
from Event.views import *

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
    path('add-flutter', add_flutter, name='add_flutter'),
    path('delete-flutter', delete_flutter, name='delete_flutter'),
    path('edit-flutter', edit_flutter, name='edit_flutter'),
    path('my-event/json', show_userevent_json, name='show_userevent_json'),
    path('music/json', show_music_json, name='show_music_json'),
    path('festival/json', show_festival_json, name='show_festival_json'),
    path('culinary/json', show_culinary_json, name='show_culinary_json'),
    path('sport/json', show_sport_json, name='show_sport_json'),
    path('culture/json', show_culture_json, name='show_culture_json'),
    path('others/json', show_others_json, name='show_others_json'),
]