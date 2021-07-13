from django.db import models
from datetime import datetime
from student_classes.models import student_class
# Create your models here.

genderChoice = (('M', 'Male'), ('F', 'Female'), ("Don't Say", "Don't Say"))
class student_detail(models.Model):
    name = models.CharField(max_length=100)
    rollNo = models.IntegerField()
    email = models.EmailField(blank=True)
    DOB = models.DateField(default=datetime.now)
    gender = models.CharField(max_length=100, choices=genderChoice)
    Age = models.IntegerField()
    class_name = models.ForeignKey(student_class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



