from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from forum.models import Question, Answer
    
class QuestionForm(ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Question Title'}), required = True)
    question = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Type your question here...'}), required = True)
    class Meta:
        model = Question
        fields = ['title', 'question']        

class AnswerForm(ModelForm):
    answer = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Type your answer here...'}), required=True)
    class Meta:
        model = Answer
        fields = ['answer']