# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Students
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from .filters import StudentsFilter
from rest_framework.views import APIView

def students_list(request):
    students = Students.objects.all()
	
    return render(request, 'school/students/students_list.html', {'students': students})

def search_student(request):
    all_students = Students.objects.all()
    student_filter = StudentsFilter(request.GET, queryset=all_students)
    return render(request, 'school/students/search_student.html', {'filter': student_filter})

def student_details(request, id):
    student = get_object_or_404(Students, id=id)
    return render(request,'school/students/student_detail.html',{'student': student})
