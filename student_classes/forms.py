from django.db.models import fields
from .models import student_class
from django import forms
from django.forms import ModelForm


class StudentClassForm(ModelForm):
    class Meta:
        model = student_class
        fields = '__all__'
        widgets = {
            'class_name': forms.TextInput(attrs={'class': 'form-control'}),
            'class_name_in_numeric':  forms.NumberInput(attrs={'class': 'form-control'}),
        }

