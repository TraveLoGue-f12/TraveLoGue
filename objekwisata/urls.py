from django.urls import path
from objekwisata.views import index, show_objekwisata

app_name = 'objekwisata'

urlpatterns = [
    path('', index, name='index'),
]