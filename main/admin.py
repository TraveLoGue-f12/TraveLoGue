from django.contrib import admin
from objekwisata.models import ObjekWisata
from Event.models import Event
from forum.models import Question, Answer
from umkm.models import UMKM
from planner.models import Trips

# Register your models here.
admin.site.register(ObjekWisata)
admin.site.register(Event)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UMKM)
admin.site.register(Trips)