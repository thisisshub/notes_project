from django.contrib.auth.models import User
import django_filters
from .models import Notes_Model

class NotesFilter(django_filters.FilterSet):
    branch_filter = django_filters.CharFilter(lookup_expr='icontains')
    file_semester_filter = django_filters.NumberFilter(lookup_expr='file_semester')
    class Meta:
        model = Notes_Model
        fields = ['branch_choice', 'file_semester']
