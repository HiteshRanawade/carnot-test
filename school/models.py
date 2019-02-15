# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=50,null=False)
    author_name = models.CharField(max_length=50,null=True)
    date_of_publication = models.DateField(null=True)
    no_of_pages = models.BigIntegerField(default=0,null=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title


class Schools(models.Model):
    region_id = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    principal = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name

class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(null=True,max_length=50)
    email = models.CharField(null=False,max_length=50)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('B', ''),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, default='B')
    school = models.ForeignKey(Schools, related_name='school',null=False, on_delete=models.CASCADE)
    books = models.ForeignKey(Books, related_name='books',blank = True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.first_name
