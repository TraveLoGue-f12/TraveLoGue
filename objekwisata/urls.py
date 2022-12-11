from django.urls import path
from objekwisata.views import index, show_objekwisata_json, add_objekwisata_ajax, add_flutter

app_name = 'objekwisata'

urlpatterns = [
    path('', index, name='index'),
    path('json/', show_objekwisata_json, name='show_objekwisata_json'),
    path('add_objekwisata_ajax/', add_objekwisata_ajax, name='add_objekwisata_ajax'),
    path('add_flutter/', add_flutter, name='add_flutter'),
]