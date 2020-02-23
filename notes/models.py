from django.db import models
from django.contrib.auth.admin import User
from django.urls import reverse
from django.utils import timezone
import datetime

branch_choices = [
    ('Computer Science Engineering', 'Computer Science Engineering' ),
    ('Civil Engineering', 'Civil Engineering'),
    ('Automobile Engineering', 'Automobile Engineering'),
    ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'),
    ('Electrical Engineering', 'Electrical Engineering'),
    ('Electronics Engineering', 'Electronics and Instrumentation'),
    ('Electrical Engineering', 'Electrical and Electronics Engineering'),
    ('Fire Engineering', 'Fire and Safety'),
    ('Information Engineering', 'Information Technology'),
    ('Mechanical Engineering', 'Mechanical Engineering'),
]

# notes semester choice from 1 to 8
semester_choice = [tuple([x,x]) for x in range(1,9)]
class Notes_Model(models.Model):
    uploader = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=2500)
    branch_choice = models.CharField(max_length=50, choices=branch_choices, default='cse')
    file_semester = models.IntegerField( choices=semester_choice)
    file = models.FileField()
    syllabus = models.TextField(max_length=200, default='No Syllabus Availibe Yet')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("notes-detail", kwargs={"pk": self.pk})

# class Comment(models.Model):
#     post = models.ForeignKey(Notes_Model, on_delete=models.CASCADE, related_name='comments', default=None)
#     author = models.CharField(max_length=200)
#     text = models.TextField(max_length=200)
#     reply = models.ForeignKey('Comment', null=True, related_name="replies", on_delete=models.CASCADE)
#     created_date = models.DateTimeField(default=timezone.now)
#     approved_comment = models.BooleanField(default=False)

#     def approve(self):
#         self.approved_comment = True
#         self.save()

#     def __str__(self):
#         return self.text

#     def approved_comments(self):
#         return self.comments.filter(approved_comment=True)

class Website_Gen(models.Model):
    c_name = models.TextField(max_length=200)
    date_established = models.DateTimeField(auto_now_add=False)
    files = models.FileField()
    syllabus = models.TextField(max_length=200, default="No Syllabus Availible Yet") 
    branch_availible = models.TextField(max_length=500)
    
    def __str__(self):
        return self.c_name
    
    def get_absolute_url(self):
        return reverse("web-gen", kwargs={"pk": self.pk})