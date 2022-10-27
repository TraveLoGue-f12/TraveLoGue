from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='home'),
    path('login/', login_user, name='login_user'),
    path('signup/', signup, name='signup'),
]