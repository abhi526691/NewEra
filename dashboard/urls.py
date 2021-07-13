from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('login/', views.index, name='index'),
    path('', views.dashboard, name='dashboard'),
    path('find-result/', views.find_result_view, name='find_result'),
    path('change-password/', views.PasswordChangeView, name='change_password'),
    path('find-result/<int:pk>/result/', views.result, name='get_result'),
    path('pdf/<int:id>/', views.pdf.as_view(), name='pdf'),
    path('examination/', views.examination)
]
