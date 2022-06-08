from django.urls import path
from . import  views

app_name = 'pdca'
urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
    path('add/', views.AddNewStudent.as_view(), name='add'),
    path('save/', views.SaveStudent.as_view(), name='save'),
    path('email/', views.send_email, name='email'),
    path('process/', views.process, name='process'),
    path('question/', views.view_list, name='list_question'),
    path('detail/<int:question_id>', views.detailView, name='detail'),
    path('<int:question_id>', views.vote, name='vote'),
]

