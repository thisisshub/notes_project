from django.urls import path, include

# viewssyllabus
from . import views 

from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    search,
    web_gen
)

# filters 
from .filters import NotesFilter
from django_filters.views import FilterView

urlpatterns = [
    path('', PostListView.as_view(), name='notes-home'),
    path('notes/new/', PostCreateView.as_view(), name='notes-create'),
    path('filter/', FilterView.as_view(filterset_class=NotesFilter, template_name='notes/templates/notes/notes/notes_model_filter.html'), name='notes-filter'),
    path('about/', views.syllabus, name='syllabus'),
    path('notes/<int:pk>', PostDetailView.as_view(), name='notes-detail'),
    path('notes/<int:pk>/update/', PostUpdateView.as_view(), name='notes-update'),
    path('website/<int:pk>/gen/', web_gen, name='web-gen'),
    path('notes/<int:pk>/delete/', PostDeleteView.as_view(), name='notes-delete'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('about/', views.about, name='notes-about'),
]