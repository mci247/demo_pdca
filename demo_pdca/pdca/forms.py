from django import  forms
from .models import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ('name', 'company', 'time_create')


class SendEmail(forms.Form):
    title = forms.CharField(max_length=100)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
    cc = forms.BooleanField(required=False)