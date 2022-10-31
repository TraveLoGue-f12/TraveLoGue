from hashlib import new
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from forum.models import Question, Answer
from forum.forms import AnswerForm, QuestionForm
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.urls import reverse
import datetime

# Create your views here.

def show_forum(request):
    question_data = Question.objects.all()
    answer_data = Answer.objects.all()
    question_form = QuestionForm()
    answer_form = AnswerForm()

    context = {
        "list_of_questions" : question_data,
        "list_of_answers" : answer_data,
        "question_form" : question_form,
        "answer_form" : answer_form,
    }
    return render(request, 'forum.html', context)

def question_json(request):
    data = Question.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def answer_json(request):
    data = Answer.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

@csrf_exempt
def add_question_ajax(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        question = request.POST.get('question')

        new_question = Question.objects.create(
            user = request.user,
            username = request.user.username,
            title = title,
            question = question,
            date = datetime.date.today()
            )
        
        result = {
            'pk': new_question.pk,
            'fields': {
                'username': new_question.user.username,
                'title': new_question.title,
                'question': new_question.question,
                'date': new_question.date
            }
        }
        return JsonResponse(result)

@csrf_exempt
def add_answer_ajax(request, pk):
    question = Question.objects.get(pk=pk)
    question.is_answered = True
    question.save()

    if request.method == "POST":
        answer = request.POST.get('answer')
        question = request.POST.get('question')

        answer = Answer.objects.create(
            user = request.user,
            username = request.user.username,
            question = question,
            answer = answer,
            date = datetime.date.today()
            )
        
        result = {
            'pk': answer.pk,
            'fields': {
                'question': answer.question,
                'answer': answer.answer,
            }
        }
        return JsonResponse(result)




        
    """ form = AnswerForm(request.POST)
    if form.is_valid():
        user = request.user
        question = get_question
        answer = request.POST.get('answer') 

        Answer.objects.create(
            user = user,
            question = question,
            answer = answer
        )

        return HttpResponseRedirect(reverse('forum:show_forum'))
else:
    form = AnswerForm()
    response = {'form': form}
    return render(request, 'add_answer.html', response) """

""" def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            title = request.POST.get('title')
            question = request.POST.get('question')

            Question.objects.create(
                user = user,
                title = title,
                question = question
            )
            return HttpResponseRedirect(reverse('forum:show_forum'))
    else:
        form = QuestionForm()
        response = {'form': form}
        return render(request, 'add_question.html', response) """
        


@csrf_exempt
def delete_forum_ajax(request, id):
    if request.method == "DELETE":
        question = get_object_or_404(Question, id = id)
        question.delete()
    return HttpResponse(status=202)