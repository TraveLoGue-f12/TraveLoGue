from django.urls import path
from requests import delete

from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('add_question/', add_question_ajax, name='add_question'),
    path('add_answer/<int:pk>', add_answer, name='add_answer'),
    path('delete_question/<id>', delete_forum, name='delete_question'),
    path('question_json/', question_json, name='question_json'),
    path('answer_json/<int:pk>', answer_json, name='answer_json'),
    path('all_answer_json/', all_answer_json, name='all_answer_json'),
    path('add_question_flutter/', add_question_flutter, name="add_question_flutter")
]