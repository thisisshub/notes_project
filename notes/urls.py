from django.urls import path, include
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('', views.home, name='notes-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='notes-home'),
    path('about/', views.about, name='notes-about'),
]