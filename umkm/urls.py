from django.urls import path
from umkm.views import *

app_name = 'umkm'

urlpatterns = [
    path('', show_data, name='rekomendasi_umkm'),
    path('delete/<int:pk>/', delete_card, name='delete_card'),
    path('json/', json_umkm, name='json_umkm'),
    path('add_umkm_ajax/', add_umkm_ajax, name='add_umkm_ajax'),
    path('shop-detail/<int:pk>/', show_umkm_by_id, name='show_umkm_by_id'),
    path('delete-ajax/<id>', delete_umkm_ajax, name='delete_umkm_ajax'),
    path('my-umkm', show_umkm_by_user, name='show_umkm_by_user'),
    path('add-flutter', add_flutter, name='add_flutter'),
    path('delete-flutter', delete_flutter, name='delete_flutter'),
    
    
]