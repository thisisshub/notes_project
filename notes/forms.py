from django import forms
from .models import Notes_Model, Web

class UploadFileForm(forms.Form):
    file = forms.FileField()

class WebForm(forms.Form):
    title = forms.CharField(label="Name of the University", max_length=200)
    year = forms.IntegerField(label_suffix="Year of Establishment")
    chancellor = forms.CharField(label="Name of the Chancellor", max_length=150)