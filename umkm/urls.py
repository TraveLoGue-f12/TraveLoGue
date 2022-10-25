from django.urls import path
from umkm.views import show_data, add_umkm

app_name = 'umkm'

urlpatterns = [
    path('', show_data, name='show_data'),
    path('add_umkm/', add_umkm, name='add_umkm')
]