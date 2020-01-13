from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'uploader': 'John Doe',
        'title': 'Computer Science III sem',
        'date_posted': 'Jan 12, 2020 ',
    },
    {
        'uploader': 'Joe Doe',
        'title': 'Mechanical Engineering II sem',
        'date_posted': 'Jan 14, 2020 ',
    }
]

def notes_login(request):
    context = {'posts': posts}
    return render(request, template_name='home.html', context=context)

def about(request):
    title = {'title': 'About'} 
    return render(request, template_name='about.html', context=title)
