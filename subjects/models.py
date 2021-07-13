from django.db import models
from django.db.models.base import Model
from student_classes.models import student_class
# Create your models here.

class subject_detail(models.Model):
    sub_name = models.CharField(max_length = 100)
    sub_code = models.CharField(max_length=100)
    sub_creation_code = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.sub_name

class subject_combination(models.Model):
    class_name = models.ForeignKey(student_class, on_delete=models.CASCADE)
    sub_name = models.ForeignKey(subject_detail, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_name + " " + self.sub_name