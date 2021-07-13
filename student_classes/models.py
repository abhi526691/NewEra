from django.db import models

# Create your models here.
class student_class(models.Model):
    class_name = models.CharField(max_length=10)
    class_name_in_numeric = models.IntegerField()
    creation_date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.class_name