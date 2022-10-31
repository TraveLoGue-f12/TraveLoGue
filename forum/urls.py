from django.urls import path
from requests import delete

from forum.views import *

app_name = "forum"

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('add_question/', add_question_ajax, name='add_question'),
    path('add_answer/<int:pk>', add_answer, name='add_answer'),
    path('delete_question/<id>', delete_forum_ajax, name='delete_question'),
    path('question_json/', question_json, name='question_json'),
    path('answer_json/<int:pk>', answer_json, name='answer_json'),
]