# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

fall = "Fall"
spring = "Spring"
Semster_choices = (
    (fall, "Fall"),
    (spring, "Spring"),
    )

# Create your models here.
class courses(models.Model):
    Course_name               = models.CharField(max_length=50, default= "course name")
    Course_code               = models.CharField(max_length=10, default= "course code")
    semester                  = models.CharField(choices=Semster_choices, max_length=50,default = fall)
    pre_reqisite              = models.CharField(default = "0", max_length=10)
    level                     = models.IntegerField(default=1)
    Taken                     = models.BooleanField(default = False)
    Does_it_have_Prerequisite = models.BooleanField(default = False)
    is_it_required            = models.BooleanField(default = False)
    
    def __str__(self):
        return self.Course_name

class student(models.Model):
    GPA             = models.FloatField(default=1.0)
    Term            = models.CharField(max_length=50, default = fall)
    student_level   = models.IntegerField(default=1)

    def __str__(self):
        return self.Term