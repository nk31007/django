from django.contrib import admin
from django.contrib.admin.filters import EmptyFieldListFilter
from django.db.models import fields
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    fields = ['eno', 'ename', 'esal']


admin.site.register(Employee, EmployeeAdmin)
