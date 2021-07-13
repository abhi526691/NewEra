from django.shortcuts import render, redirect
from .models import student_class
from .forms import StudentClassForm
# Create your views here.

def createClass(request):
    if request.method == 'POST':
        form = StudentClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/classes/list/')

    form = StudentClassForm()
    context = {'main_page_title' : 'Manage Classes', 'form':form, 'panel_name' : 'Classes', 'panel_title':'View Classes Info'}
    return render(request, 'createClass.html',context)

def updateClass(request, id):
    instance = student_class.objects.get(id=id)
    if request.method == 'POST':
        form = StudentClassForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/classes/list/')
    
    form = StudentClassForm(instance=instance)
    context = {'main_page_title' : 'Manage Classes', 'form':form, 'panel_name' : 'Classes', 'panel_title':'View Classes Info'}
    return render(request, 'createClass.html', context)

def deleteClass(request, id):
    form = student_class.objects.get(id=id)
    form.delete()
    return redirect('/classes/list/')

def listClass(request):
    form = student_class.objects.all()
    field_list = [
        'Class Name', 'Class Name In Numeric', 'Creation Date'
    ]

    context = {'main_page_title' : 'Manage Classes', 'form':form, 'panel_name' : 'Classes', 'panel_title':'View Classes Info', 'field_list':field_list}

    return render(request, 'listClass.html',context)

