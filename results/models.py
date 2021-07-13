from django.db import models
from django.contrib.postgres.fields import JSONField
from student_classes.models import student_class
from students.models import student_detail
# Create your models here.

class DeclareResult(models.Model):
    class_name = models.ForeignKey(student_class, on_delete=models.CASCADE)
    student_name = models.ForeignKey(student_detail, on_delete=models.CASCADE)
    marks = JSONField(blank=True)

    def __str__(self):
        return self.class_name.class_name


