from django import forms
from django.db import models
from django.db.models import fields 
from django.forms import ModelForm, widgets
from .models import subject_detail, subject_combination

class SubjectDetailForm(ModelForm):
    class Meta:
        model = subject_detail
        fields = '__all__'
        widgets = {
            'sub_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'sub_code' : forms.TextInput(attrs={'class' : 'form-control'}),
        }

class SubjectCombinationForm(ModelForm):
    class Meta:
        model = subject_combination
        fields = '__all__'
        widgets = {
            'class_name' : forms.Select(attrs={'class' : 'form-control'}),
            'sub_name' : forms.Select(attrs={'class' : 'form-control'})
        }