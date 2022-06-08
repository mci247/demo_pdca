from django.shortcuts import render
from django.http import  HttpResponse
from .forms import StudentForm, SendEmail
from django.views import View
from .models import Question

# Create your views here.


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

def view_list(request):
    list_question = Question.objects.all()
    context = {'dsquest': list_question}
    return render(request, "pdca/question_list.html", context)

def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    context = {'qs': q}
    return render(request, "pdca/detail_question.html", context)

def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        dulieu = request.POST['choice']
        c = q.choice_set.get(pk=dulieu)

    except:
        HttpResponse("Lỗi không có choice")
    c.vote = c.vote + 1
    c.save()
    context = {'q': q}
    return render(request, "pdca/result.html", context)