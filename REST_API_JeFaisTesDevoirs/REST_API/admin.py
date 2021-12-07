# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from REST_API.models import Subject, Answer

# Register your models here.

class ValueSubject(admin.ModelAdmin):
    list_display = ('id', 'Answered', 'UserRef', 'Price', 'hasPaid')

class ValueAnswer(admin.ModelAdmin):
    list_display = ('id', 'SubjectRef', 'UserRef', 'isValid', 'isPending', 'isPaid')

admin.site.register(Subject, ValueSubject)
admin.site.register(Answer, ValueAnswer)