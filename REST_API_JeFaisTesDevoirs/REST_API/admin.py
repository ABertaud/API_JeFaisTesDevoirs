# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from REST_API.models import Subject, Answer, File

# Register your models here.

class ValueFile(admin.ModelAdmin):
    list_display = ('id', 'file')

class ValueSubject(admin.ModelAdmin):
    list_display = ('id', 'FileRef', 'Answered', 'UserRef', 'Price', 'hasPaid')

class ValueAnswer(admin.ModelAdmin):
    list_display = ('id', 'FileRef', 'SubjectRef', 'UserRef', 'isValid', 'isPending', 'isPaid')

admin.site.register(File, ValueFile)
admin.site.register(Subject, ValueSubject)
admin.site.register(Answer, ValueAnswer)