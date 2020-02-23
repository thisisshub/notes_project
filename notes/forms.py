from django import forms
from .models import Notes_Model

class UploadFileForm(forms.Form):
    file = forms.FileField()

# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comment
#         fields = ('author', 'text',)