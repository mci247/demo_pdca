from django.contrib import admin
from .models import Students, Question, Choice

# Register your models here.
admin.site.register(Students)
admin.site.register(Question)
admin.site.register(Choice)