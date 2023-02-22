from django import forms
from django.forms import ModelForm
from . models import QA

class QAForm(ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"} ) )
    ques = forms.CharField(max_length=500, widget=forms.Textarea(attrs={"class": "form-control"} ) )
    ans = forms.CharField(max_length=500, blank=True, null=True, widget=forms.Textarea(attrs={"class": "form-control"} ) )


    class Meta:
        model = QA
        fields = ['name', 'ques', 'ans']