from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Notes_Model

def home(request):
    context = {'posts': Notes_Model.objects.all}
    ordering = ['-date_posted']
    return render(request, template_name='home.html', context=context, filter=ordering)

class PostListView(ListView):
    model = Notes_Model
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Notes_Model
    # template_name = 'templates/notes/notes/notes_model_list.html'
    # context_object_name = 'posts'
    # ordering = ['-date_posted']

def about(request):
    title = {'title': 'About'} 
    return render(request, template_name='about.html', context=title)
