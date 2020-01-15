from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Notes_Model
from django.contrib.auth.decorators import login_required
from users.forms import UploadFileForm

def home(request):
    context = {'posts': Notes_Model.objects.all}
    return render(request, template_name='home.html', context=context)

class PostListView(ListView):
    model = Notes_Model
    template_name = 'template/notes/notes/note_model_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Notes_Model

class PostCreateView(CreateView):
    model = Notes_Model
    # template_name = 'template/notes/notes/note_model_form.html'
    fields = ['title', 'description', 'file_semester', 'branch_choice', 'file']
    
    @login_required
    def upload_file(self, request):
        if (request.method == 'POST'):
            form = Notes_Model(request.POST, request.FILES)
            if form.is_valid():
                instance = Notes_Model(file_field=request.FILES['file'])
                instance.save()
                return redirect('notes-create')
            else:
                pass
            
    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)

def about(request):
    title = {'title': 'About'} 
    return render(request, template_name='about.html', context=title)
