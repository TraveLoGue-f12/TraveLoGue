import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.backends import UserModel
from main.models import Profile


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
                "status": True,
                "message": "Successfully Logged In!"
                # Insert any extra data if you want to pass data to Flutter
                }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Failed to Login, Account Disabled."
                }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Failed to Login, check your email/password."
            }, status=401)

@csrf_exempt
def get_data(request):
    data = json.loads(request.body)
    print(data)
    username = data['username1']
    password = data['password1']
    user = authenticate(username=username, password=password)
    userProfile =  Profile.objects.filter(user=user)
   
    return JsonResponse({
        "status": str(userProfile.values()[0]['status']),
        "full_name": str(userProfile.values()[0]['full_name']),
        "email" : str(userProfile.values()[0]['email']),
        })
    
@csrf_exempt
def register(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        
        full_name = data["full_name"]
        email = data["email"]
        password1 = data["password1"]
        password2 = data["password2"]
        status = data["status"]
        username = data["username"]
        
        if UserModel.objects.filter(username=username).exists():
            return JsonResponse({"status": "duplicate"}, status=401)

        if password1 != password2:
            return JsonResponse({"status": "pass failed"}, status=401)

        createUser = UserModel.objects.create_user(
        username = username, 
        password = password1,
        )

        


        createUser.save()
        newUser = Profile.objects.create(
        user = createUser, 
        email = email,
        status = status,
        full_name = full_name
        )

        newUser.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)