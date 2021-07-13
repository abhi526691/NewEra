from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    CreateView, ListView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import DeclareResult
from .forms import DeclareResultForm
from subjects.models import subject_combination
from students.models import student_detail
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from student_classes.models import student_class
import json
from django.contrib.auth.decorators import login_required
# Create your views here.
    

def validate_data(request):
    smt = subject_combination.objects.all()
    data = {}
    if request.method == "GET":
        rc = request.GET['selectedClass']
        subjects = []
        for s in smt:
            if s.class_name.class_name in rc:
                subjects.append(s.sub_name)
        sir_subjects = serializers.serialize('json', subjects)
        data['subjects'] = sir_subjects
        return JsonResponse(data)
    subjects = None
    data['result'] = 'you made a request with empty data'
    return HttpResponse(json.dumps(data), content_type="application/json")


def declare_result_view(request):
    context = {}
    if request.method == "POST":
        form = request.POST
        data = json.loads(json.dumps(form))
        data.pop('csrfmiddlewaretoken')
        pk = data['class_name']
        clas = student_class.objects.get(id=pk)
        pk = data['student_name']
        student = student_detail.objects.get(id=pk)
        data.pop('class_name')
        data.pop('student_name')
        DeclareResult.objects.create(class_name=clas, student_name=student, marks=data)
    else:
        form = DeclareResultForm()
        context['main_page_title'] = 'Declare Students Result'
        context['panel_name'] = 'Results'
        context['panel_title'] = 'Declare Result'
        context['form'] = form
    return render(request, "declareResult.html", context)

def setup_update_view(request):
    data = {}
    if request.method == "GET":
        pk_value = int(request.GET['pk_value'])
        result_obj = get_object_or_404(DeclareResult, pk = pk_value)
        dt = result_obj.marks
        data['dt'] = dt
        return HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponse(json.dumps(data), content_type="application/json")

@login_required
def result_update_view(request, pk):
    result = get_object_or_404(DeclareResult, pk=pk)
    form = DeclareResultForm(instance=result)
    context = {}
    context['main_page_title'] = 'Update Students Result'
    context['panel_name'] = 'Results'
    context['panel_title'] = 'Update Result'
    context['form'] = form
    context['pk'] = pk
    if request.method == "POST":
        all_data = request.POST
        data = json.loads(json.dumps(all_data))
        data.pop('csrfmiddlewaretoken')
        pk = data['class_name']
        clas = student_class.objects.get(id=pk)
        pk = data['student_name']
        student = student_detail.objects.get(id=pk)
        data.pop('class_name')
        data.pop('student_name')
        print('Modified Data = ', data)
        result.class_name = clas
        result.student_name = student
        result.marks = data
        result.save()
        print('\nResult updated\n')
        return redirect('results:result_list')
    return render(request, "updateResult.html", context)

@login_required
def result_delete_view(request, pk):
    obj = DeclareResult.objects.get(id = pk)
    obj.delete()
    return redirect('/results/list/')


def DeclareResultListView(request):
    form = DeclareResult.objects.all()
    field_list = [
        'Student Name', 'Roll No', 'Class', 'View Result'
    ]
    context = {'form' : form, 'main_page_title' : 'Manage Results', 'panel_name' : 'Results', 'panel_title' : 'View Results Info', 'field_list' : field_list}
    return render(request, 'listResult.html', context)