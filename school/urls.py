from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.students_list, name='students_list'),
    url(r'^search/$', views.search_student, name='seach student'),
    url(r'^student/(?P<id>\d+)/$', views.student_details, name='student_detail'),
]