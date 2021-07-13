from django.urls import path
from .views import createStudent, updateStudent, deleteStudent, listStudent
app_name = 'students'

urlpatterns = [
    path('create/', createStudent, name='student_create'),
    path('update/<int:id>/',updateStudent, name='student_update'),
    path('delete/<int:id>/', deleteStudent, name='student_delete'),
    path('list/', listStudent, name='student_list')
]