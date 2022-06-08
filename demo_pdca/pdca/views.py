from django.shortcuts import render
from django.http import  HttpResponse
from .forms import StudentForm, SendEmail
from django.views import View

# Create your views here.

def test_func(request):
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

def send_email(request):
    b = SendEmail()
    return render(request, 'pdca/email.html', {'f': b})

def process(request):
    if request.method == 'POST':
        m = SendEmail(request.POST)
        if m.is_valid():
            context2 = {'email_data': m}
            return render(request, 'pdca/recipient_email.html', context2)
        else:
            return HttpResponse('Form not validate')
    else:
        return HttpResponse('Khong phai POST method')