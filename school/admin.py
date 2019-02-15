# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import Schools, Students, Books
# Register your models here.


@admin.register(Books)
class BooksAdmin(ImportExportModelAdmin):
    list_display = ['title', 'author_name', 'date_of_publication','no_of_pages']

@admin.register(Schools)
class SchoolsAdmin(ImportExportModelAdmin):
    list_display = ['region_id', 'name', 'email', 'principal', 'phone', 'address']

@admin.register(Students)
class StudentsAdmin(ImportExportModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'gender', 'school', 'books']
