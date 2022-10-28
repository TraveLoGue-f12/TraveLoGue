from django.urls import path
from requests import delete

from forum.views import add_question_ajax, show_forum, add_question, add_answer, show_json, delete_task

app_name = "forum"

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('add_question/', add_question, name='add_question'),
    path('add_answer/<int:pk>', add_answer, name='add_answer'),
    path('json/', show_json, name='show_json'),
    path('add/', add_question_ajax, name='add_question_ajax'),
    path('delete/<int:pk>', delete_task, name='delete_task'),
]