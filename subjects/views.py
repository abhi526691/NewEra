from django.shortcuts import render, redirect
from .models import subject_detail, subject_combination
from .forms import SubjectDetailForm, SubjectCombinationForm
# Create your views here.

def addSubject(request):
    if request.method == 'POST':
        form = SubjectDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/subjects/list/')
    form = SubjectDetailForm()
    context = {'main_page_title' : 'Add Subject', 'form':form, 'panel_name' : 'Subjects', 'panel_title':'Add Subject'}
    return render(request, 'addSubject.html', context)

def updateSubject(request, id):
    instance = subject_detail.objects.get(id=id)
    if request.method == 'POST':
        form = SubjectDetailForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/subjects/list/')

    form = SubjectDetailForm(instance=instance)
    context = {'main_page_title' : 'Update Subject', 'form':form, 'panel_name' : 'Subjects', 'panel_title':'Update Subject Info'}
    return render(request, 'addSubject.html', context)

def deleteSubject(request, id):
    form = subject_detail.objects.get(id=id)
    form.delete()
    return redirect('/subjects/list/')

def listSubject(request):
    form = subject_detail.objects.all()
    field_list = [
        'sub_name', 'sub_code']
    context = {'main_page_title' : 'Manage Subjects', 'form':form, 'panel_name' : 'Subjects', 'panel_title':'View Subject Info', 'field_list' : field_list}
    return render(request, 'listSubject.html', context)


def addSubjectCombination(request):
    if request.method == 'POST':
        form = SubjectCombinationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/subjects/combination/list/')
    form = SubjectCombinationForm()
    context = {'main_page_title' : 'Add Subject Combination', 'form':form, 'panel_name' : 'Subject Combination', 'panel_title':'Add Subject Combinations'}
    return render(request, 'addSubjectCombination.html', context)

def updateSubjectCombination(request, id):
    instance = subject_combination.objects.get(id=id)
    if request.method == 'POST':
        form = SubjectCombinationForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/subjects/combination/list/')

    form = SubjectCombinationForm(instance=instance)
    context = {'main_page_title' : 'Update Subject Combination', 'form':form, 'panel_name' : 'Subjects Combination', 'panel_title':'Update Subject Combination Info'}
    return render(request, 'addSubjectCombination.html', context)

def deleteSubjectCombination(request, id):
    form = subject_combination.objects.get(id=id)
    form.delete()
    return redirect('/subjects/combination/list/')

def listSubjectCombination(request):
    form = subject_combination.objects.all()
    field_list = [
        'Class_Name', 'Subject_Name'
    ]
    context = {'main_page_title' : 'Manage Subject Combination', 'form':form, 'panel_name' : 'Subject Combination', 'panel_title':'View Subject Combination Info', 'field_list' : field_list}
    return render(request, 'listSubjectCombination.html', context)

