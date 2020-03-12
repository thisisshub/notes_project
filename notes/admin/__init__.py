from django.contrib import admin
from notes.models import Notes_Model, Web


@admin.register(Notes_Model)
class Notes_ModelAdmin(admin.ModelAdmin):
    """
    """
    list_display = (
        'id', 'uploader', 'title', 'date_posted', 'branch_choice', 'file_semester',
    )
    search_fields = (
        'uploader', 'title', 'branch_choice',
    )
    

class WebAdmin(admin.ModelAdmin):
    """
    """
    list_display = (
        'title', 'year', 'chancellor',
    )