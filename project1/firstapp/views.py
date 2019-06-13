from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import studentforms
from firstapp import forms
# Create your views here.
def studentview(request):
    form=forms.studentforms()
    return render(request,'firstapp/register.html',{'form':forms})
