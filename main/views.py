from main.models import Profile
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect
from main.forms import SignUpForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("main:index")) # membuat response
            return response
        else:
            messages.info(request, 'Invalid username/password!')
            
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = redirect('main:index')
    return response

def signup(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            Profile.objects.create(
                user = new_user,
                status = new_user.status,
                full_name = new_user.full_name,
                email = new_user.email
                )
            messages.success(request, 'Sign up successful!')
            return redirect('main:login_user')
    
    context = {'form':form}
    return render(request, 'signup.html', context)

