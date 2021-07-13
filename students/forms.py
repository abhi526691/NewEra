from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import student_detail

class StudentDetailForm(ModelForm):
    class Meta:
        model = student_detail
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'rollNo':  forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'DOB' : forms.DateInput(attrs={'class':'form-control'}),
            'gender' : forms.Select(attrs={'class':'form-control'}),
            'Age' : forms.NumberInput(attrs={'class':'form-control'}),
            'class_name' : forms.Select(attrs={'class' : 'form-control'})
        }