from django.urls import path
from . import  views

app_name = 'pdca'
urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
    path('add/', views.AddNewStudent.as_view(), name='add'),
    path('save/', views.SaveStudent.as_view(), name='save'),
    path('email/', views.send_email, name='email'),
    path('process/', views.process, name='process'),
    path('test/', views.test_func, name='testfunc'),
]

