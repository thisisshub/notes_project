from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.notes_login, name='notes-login'),
    path('about/', views.about, name='notes-about'),
]