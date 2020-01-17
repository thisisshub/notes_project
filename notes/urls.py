from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views 

urlpatterns = [
    path('', PostListView.as_view(), name='notes-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('notes/new/', PostCreateView.as_view(), name='notes-create'),
    path('notes/<int:pk>', PostDetailView.as_view(), name='notes-detail'),
    path('notes/<int:pk>/update/', PostUpdateView.as_view(), name='notes-update'),
    path('notes/<int:pk>/delete/', PostDeleteView.as_view(), name='notes-delete'),
    path('about/', views.about, name='notes-about'),
]