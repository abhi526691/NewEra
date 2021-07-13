from django.shortcuts import render, redirect
from .models import student_detail
from .forms import StudentDetailForm
# Create your views here.

def createStudent(request):
    if request.method == 'POST':
        form = StudentDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/students/list/')
    form = StudentDetailForm()
    context = {'form' : form, 'main_page_title' : 'Add Student', 'panel_name' : 'Student', 'panel_title':'Add Student Info'}
    return render(request, 'addStudent.html', context)

def updateStudent(request, id):
    instance = student_detail.objects.get(id=id)
    if request.method == 'POST':
        form = StudentDetailForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/students/list/')

    form = StudentDetailForm(instance=instance)
    context = {'form' : form, 'main_page_title' : 'Update Student', 'panel_name' : 'Student', 'panel_title':'Update Student Info'}
    return render(request, 'addStudent.html', context)

def deleteStudent(request, id):
    form = student_detail.objects.get(id=id)
    form.delete()
    return redirect('/students/list/')

def listStudent(request):
    form = student_detail.objects.all()
    field_list = ['Name', 'rollNo', 'Email', 'class','DOB', 'Age', 'Gender']
    context = {'form' : form, 'main_page_title' : 'Total Student', 'panel_name' : 'Student', 'panel_title':'Total Student Info', 'field_list':field_list}
    return render(request, 'listStudent.html', context)








