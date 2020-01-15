from django.db import models
from django.contrib.auth.admin import User

class Notes_Model(models.Model):
    uploader = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    branch = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
