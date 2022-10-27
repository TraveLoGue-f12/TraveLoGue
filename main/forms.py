from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    isTourist = forms.BooleanField()
    fullName = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ['isTourist', 'fullName', 'username', 'email', 'password1']

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.isTourist = self.cleaned_data["isTourist"]
        user.fullName = self.cleaned_data["fullName"]
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        
        return user