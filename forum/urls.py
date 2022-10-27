from django.urls import path

from forum.views import *

app_name = "urls"

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('add_question/', add_question, name='add_question'),
    path('json/', show_json, name='show_json'),
]