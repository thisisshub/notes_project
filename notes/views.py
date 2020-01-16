from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Notes_Model
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from django.contrib import messages

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

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Notes_Model
    # template_name = 'template/notes/notes/note_model_form.html'
    fields = ['title', 'description', 'file_semester', 'branch_choice', 'file']

    @login_required
    def upload_file(self, request):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, f'Your files have been uploaded')
                return redirect('notes-home')

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notes_Model
    # template_name = 'template/notes/notes/note_model_form.html'
    fields = ['title', 'description', 'file_semester', 'branch_choice', 'file']

    @login_required
    def upload_file(self, request):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('notes-detail')
    
    def test_func(self):
        post = self.get_object()
        if (self.request.user == post.uploader):
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notes_Model
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.uploader:
            return True
        return False

def about(request):
    title = {'title': 'About'} 
    return render(request, template_name='about.html', context=title)
