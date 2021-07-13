from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import DeclareResult

class DeclareResultForm(ModelForm):
    class Meta:
        model = DeclareResult
        fields = ['class_name', 'student_name']
        widgets = {
            'class_name' : forms.Select({'class' : 'form-control'}),
            'student_name' : forms.Select({'class' : 'form-control'})
        }