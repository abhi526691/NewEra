from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse, JsonResponse
from io import BytesIO
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
from results.models import DeclareResult
from django.urls import reverse_lazy
from django.core import serializers
import json
from io import StringIO
from django.http import Http404
from results.models import DeclareResult
from student_classes.models import student_class
from subjects.models import subject_detail
from students.models import student_detail
# Create your views here.

def dashboard(request):
    TotalClass = student_class.objects.all()
    TotalSubject = subject_detail.objects.all()
    TotalStudent = student_detail.objects.all()
    TotalResult = DeclareResult.objects.all()
    context = {'TotalClass' : TotalClass, 'TotalSubject' : TotalSubject, 'TotalStudent' : TotalStudent, 'TotalResult' : TotalResult}
    return render(request, 'dashboard.html', context)

def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:dashboard')
        else:
            context = {'message':'Invalid User Name and Password'}
            return render(request, 'indexPage.html', context)
    return render(request, 'indexPage.html', {'name': 'Abhishek Pandey', 'pass': 'login@NewEra'})


def logoutPage(request):
    logout(request)
    return redirect('/')

def find_result_view(request):
    student_class = DeclareResult.objects.all()
    if request.method == "POST":
        data = request.POST
        # data = json.loads(form)
        roll = int(data['rollid'])
        pk = int(data['class'])
        clss = get_object_or_404(DeclareResult, pk=pk)
        if clss.student_name.rollNo == roll:
            data = {
                'pk': data['class']
            }
            return JsonResponse(data)
        else:
            pk = '0'
            data = {
                'pk': pk
            }
            return JsonResponse(data)
    return render(request, 'find_result.html', {'class':student_class})


def result(request, pk):
    object = get_object_or_404(DeclareResult, pk=pk)
    lst = []
    marks = []
    gradePoint = []
    for i in range(int(len(object.marks)/2)):
        lst.append(object.marks['subject_'+str(i)])
        lst.append(object.marks['subject_'+str(i)+'_mark'])
        marks.append(lst)
        lst = []
    for i in marks:
        if int(i[1]) >= 90 and int(i[1]) <= 100:
            gradePoint.append('A+')
        elif int(i[1]) >= 80 and int(i[1]) < 90:
            gradePoint.append('A')
        elif int(i[1]) >= 70 and int(i[1]) < 80:
            gradePoint.append('B+')
        elif int(i[1]) >= 60 and int(i[1]) < 70:
            gradePoint.append('B')
        elif int(i[1]) >= 50 and int(i[1]) < 60:
            gradePoint.append('C+')
        elif int(i[1]) >= 40 and int(i[1]) < 50:
            gradePoint.append('C')
        elif int(i[1]) >= 30 and int(i[1]) < 40:
            gradePoint.append('D+')
        elif int(i[1]) >= 20 and int(i[1]) < 30:
            gradePoint.append('D')
        else:
            gradePoint.append('E')
    
    return render(request, 'result.html', {'object':object,'pk':pk, 'marks':marks, 'gradePoint' : gradePoint})


def PasswordChangeView(request):
    return render(request, 'password_change_form.html', context={'main_page_title' : 'Admin Change Password', 'panel_title' : 'Admin Change Password'})



def renderPdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


class pdf(View):
    def get(self, request, id):
        try:
            query = get_object_or_404(DeclareResult, id=id)
        except:
            Http404('Content Not Found')
        marks = []
        lst = []
        for i in range(int(len(query.marks)/2)):
            lst.append(query.marks['subject_'+str(i)])
            lst.append(query.marks['subject_'+str(i)+'_mark'])
            marks.append(lst)
            lst = []
        article_pdf = renderPdf('result.html', {'object': query, 'marks':marks})
        return HttpResponse(article_pdf, content_type='application/pdf')

def examination(request):
    return render(request, 'examination.html')


