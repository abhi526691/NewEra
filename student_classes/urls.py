from django.urls import path
from .views import createClass, updateClass, deleteClass, listClass

app_name = 'classes'
urlpatterns = [
    path('create/', createClass, name='create'),
    path('update/<int:id>/',updateClass, name='update'),
    path('delete/<int:id>/',deleteClass, name='delete'),
    path('list/', listClass, name='list')
]