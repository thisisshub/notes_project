from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='notes-home'),
    path('', ,name='upload')
    path('notes/<int:pk>', PostDetailView.as_view(), name='notes-detail'),
    path('notes/new/', PostCreateView.as_view(), name='notes-create'),
    path('about/', views.about, name='notes-about'),
]