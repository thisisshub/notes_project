from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Notes_Model
from django.contrib.auth.decorators import login_required

from .forms import UploadFileForm
from django.contrib import messages

from django.conf.urls import url
from django.contrib.auth.models import User

from django.core.paginator import Paginator

from .filters import NotesFilter

# file transfer
import os
from django.conf import settings
from django.core.files import File

def home(request):
    context = {'posts': Notes_Model.objects.all}
    return render(request, template_name='home.html', context=context)


def about(request):
    title = {'title': 'About'} 
    return render(request, template_name='about.html', context=title)
    
class PostListView(ListView):
    model = Notes_Model
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

class PostDetailView(DetailView):
    model = Notes_Model

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Notes_Model
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
        if self.request.user == post.uploader:
            return True
        return False

class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Notes_Model
    success_url = '/'

    def test_func(self):
        """
        change second self.request.user to document.uploader
        """
        if (self.request.user == self.request.user):
            return True
        return False

def search(request):
    branch_list = Notes_Model.objects.all()
    branch_filter = NotesFilter(request.GET, queryset=Notes_Model)
    return render(request, 'notes/templates/notes/notes/notes_model_filter.html', {'filter': branch_filter})

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type=None)
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
        raise Http404