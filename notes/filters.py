from django.contrib.auth.models import User
import django_filters
from .models import Notes_Model

class NotesFilter(django_filters.FilterSet):
    class Meta:
        model = Notes_Model
        fields = ['branch_choice', 'file_semester']