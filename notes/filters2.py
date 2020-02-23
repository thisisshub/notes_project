import django_filters
from .models import Notes_Model, Website_Gen

class WebFilter(django_filters.FilterSet):

    class Meta:
        model = Website_Gen
        fields = ['c_name']

        