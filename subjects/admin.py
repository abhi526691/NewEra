from django.contrib import admin
from django.contrib.admin.sites import site
from .models import subject_detail, subject_combination
# Register your models here.

admin.site.register(subject_combination)
admin.site.register(subject_detail)
