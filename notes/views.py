from django.shortcuts import render
from django.http import HttpResponse
from .models import Notes_Model

def home(request):
    context = {'posts': Notes_Model.objects.all}
    return render(request, template_name='home.html', context=context)

def about(request):
    title = {'title': 'About'} 
    return render(request, template_name='about.html', context=title)
