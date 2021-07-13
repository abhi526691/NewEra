from django.urls import path
from .views import addSubject, addSubjectCombination, updateSubject, updateSubjectCombination, deleteSubject, deleteSubjectCombination, listSubject, listSubjectCombination
app_name = 'subjects'

urlpatterns = [
    path('create/', addSubject, name='subject_create'),
    path('update/<int:id>/', updateSubject, name='subject_update'),
    path('delete/<int:id>/', deleteSubject, name='subject_delete'),
    path('list/', listSubject, name='subject_list'),
    path('combination/create/',addSubjectCombination, name='subject_create_combination'),
    path('combination/update/<int:id>/', updateSubjectCombination, name='subject_update_combination'),
    path('combination/delete/<int:id>/', deleteSubjectCombination, name='subject_delete_combination'),
    path('combination/list/', listSubjectCombination, name='subject_list_combination')
]