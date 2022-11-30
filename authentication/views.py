import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.backends import UserModel


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
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        full_name = data["full_name"]
        email = data["email"]
        password1 = data["password1"]
        status = data["status"]
        username = data["username"]

        newUser = UserModel.objects.create_user(
        username = username, 
        email = email,
        password = password1,
        status = status,
        full_name = full_name
        )

        newUser.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)