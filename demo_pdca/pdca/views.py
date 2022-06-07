from django.shortcuts import render
from django.http import  HttpResponse
from .forms import StudentForm
from django.views import View

# Create your views here.

def test_func(reques):
    return  HttpResponse("Đây là hàm test")

class IndexClass(View):
    def get(self, request):
        return HttpResponse('Xin chào')

class AddNewStudent(View):
    def get(self, request):
        a = StudentForm()
        context = {'f': a}
        return render(request, 'pdca/add_students.html', context)

class SaveStudent(View):
    def post(self, request):
        g = StudentForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('Lưu oke')
        else:
            return HttpResponse('Không được validate')
