from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from forum.forms import AnswerForm, QuestionForm
from forum.models import Question, Answer
from django.core import serializers
from django.shortcuts import render
from django.urls import reverse
from main.models import Profile
import datetime
import json


# Create your views here.

def show_forum(request):
    question_data = Question.objects.all()
    answer_data = Answer.objects.all()
    question_form = QuestionForm()
    user = request.user

    context = {
        'list_of_questions': question_data,
        'list_of_answers': answer_data,
        'question_form': question_form,
        'user_status' : '',
        'user_loggedin': user.username,
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

def all_answer_json(request):
    data = Answer.objects.all()
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

@login_required(login_url='/login/')
@csrf_exempt
def add_answer(request, pk):
    get_question = Question.objects.get(pk=pk)
    get_question.is_answered = True
    get_question.save()

    if request.method == 'POST':
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

@login_required(login_url='/login/')
@csrf_exempt
def delete_forum(request, id):
    Question.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse('forum:show_forum'))

@csrf_exempt
def add_question_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        
        title = data["title"]
        question = data["question"]

        try:
            Question.objects.get(title=title, question=question)
            return JsonResponse({"status": "dup"}, status=401)
        except:
            add_question = Question.objects.create(
                user = request.user, 
                username = request.user.username,
                date = datetime.date.today(),
                title = title,
                question = question,
                is_answered = False,
            )

            add_question.save()
        
            return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def add_answer_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        
        question = data["question"]
        answer = data["answer"]

        try:
            Answer.objects.get(answer=answer)
            return JsonResponse({"status": "dup"}, status=401)
        except:
            add_answer = Answer.objects.create(
                user = request.user, 
                username = request.user.username,
                question = question,
                date = datetime.date.today(),
                answer = answer,
            )

            add_answer.save()
        
            return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
