from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from forum.models import Question, Answer
from forum.forms import AnswerForm, QuestionForm
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.urls import reverse
from main.models import Profile
import datetime

# Create your views here.

def show_forum(request):
    question_data = Question.objects.all()
    answer_data = Answer.objects.all()
    question_form = QuestionForm()
    user = request.user
    context = {
        "list_of_questions" : question_data,
        "list_of_answers" : answer_data,
        "question_form" : question_form,
        "user_status" : "",
        "user": user.username
    }

    if user.is_authenticated:
        profile = Profile.objects.get(user=user)
        context['user_status'] = profile.status
    
    return render(request, 'forum.html', context)

def question_json(request):
    data = Question.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def answer_json(request, pk):
    question = Question.objects.get(pk=pk)

    data = Answer.objects.filter(question=question)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')
    
@login_required(login_url='/login/')
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

""" @csrf_exempt
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
        return JsonResponse(result) """

@login_required(login_url='/login/')
@csrf_exempt
def add_answer(request, pk):
    get_question = Question.objects.get(pk=pk)
    get_question.is_answered = True
    get_question.save()

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            user = request.user
            question = get_question
            answer = request.POST.get('answer') 
            date = datetime.date.today()

            Answer.objects.create(
                user = user,
                username = request.user.username,
                question = question,
                answer = answer,
                date = date
            )

            question.is_answered = True
            return HttpResponseRedirect(reverse('forum:show_forum'))
    else:
        form = AnswerForm()
        response = {'form': form}
        return render(request, 'add_answer.html', response)
        
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
        

@login_required(login_url='/login/')
@csrf_exempt
def delete_forum(request, id):
    Question.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse('forum:show_forum'))