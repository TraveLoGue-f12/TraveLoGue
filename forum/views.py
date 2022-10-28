from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from forum.models import Question, Answer
from forum.forms import AnswerForm, QuestionForm
from django.core import serializers
from django.urls import reverse

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
        "username" : request.user.username
    }
    return render(request, 'forum.html', context)

""" def add_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            user = request.user
            title = request.POST.get('title')
            question = request.POST.get('question')

            Question.objects.create(
                user = user,
                title = title,
                question = question
            )

            return JsonResponse({
                'error' : False,
                'msg' : 'Successful'
            }) """

def add_question_ajax(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        question = request.POST.get('question')
        user = request.user

        Question.objects.create(user=user, title=title, question=question)
        return JsonResponse({'error': False})

def add_question(request):
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
        return render(request, 'add_question.html', response)
        
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

            Answer.objects.create(
                user = user,
                question = question,
                answer = answer
            )

            return HttpResponseRedirect(reverse('forum:show_forum'))
    else:
        form = AnswerForm()
        response = {'form': form}
        return render(request, 'add_answer.html', response)

def delete_task(request, pk):
    Question.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('forum:show_forum'))

def show_json(request):
    data = Question.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')