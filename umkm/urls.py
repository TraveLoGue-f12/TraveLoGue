from django.urls import path
from umkm.views import *

app_name = 'umkm'

urlpatterns = [
    path('', show_data, name='rekomendasi_umkm'),
    path('add_umkm/', add_umkm, name='add_umkm'),
    path('delete/<int:pk>/', delete_card, name='delete_card'),
    path('json/', json_umkm, name='json_umkm')
]