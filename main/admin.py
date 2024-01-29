from django.contrib import admin
from .models import *

# региструем модели что бы их было видно в админке
admin.site.register(Student)
admin.site.register(Results)

