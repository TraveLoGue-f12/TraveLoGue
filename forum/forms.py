from django import forms
from django.forms import ModelForm
from forum.models import Question, Answer
    
class QuestionForm(ModelForm):
    title = forms.CharField(widget = forms.TextInput, required=True)
    question = forms.CharField(widget = forms.Textarea, required=True)
    class Meta:
        model = Question
        fields = ["title", "question"]        

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ["answer"]