from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from forum.models import Question, Answer
from forum.forms import AnswerForm, QuestionForm
from django.core import serializers

# Create your views here.

def show_forum(request):
    question_data = Question.objects.all().values()
    answer_data = Answer.objects.all().values()

    context = {
        "list_of_questions" : question_data,
        "list_of_answers" : answer_data
    }
    return render(request, 'forum.html', context)

def add_question(request):
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
            })

def add_answer(request, pk):
    get_question = Question.objects.get(pk=pk)

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

            question.is_answered = True

            return JsonResponse({
                'error' : False,
                'msg' : 'Successful'
            })

def show_json(request):
    data = Question.objects.all().values()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')