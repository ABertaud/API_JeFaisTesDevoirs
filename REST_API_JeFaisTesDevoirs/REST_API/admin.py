# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from REST_API.models import CustomUser, Subject, Answer, File

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email')
    list_filter = ('username', 'email')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_superuser', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class ValueFile(admin.ModelAdmin):
    list_display = ('id', 'file')

class ValueSubject(admin.ModelAdmin):
    list_display = ('id', 'FileRef', 'Answered', 'UserRef', 'Price', 'hasPaid')

class ValueAnswer(admin.ModelAdmin):
    list_display = ('id', 'FileRef', 'SubjectRef', 'UserRef', 'isValid', 'isPending', 'isPaid')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(File, ValueFile)
admin.site.register(Subject, ValueSubject)
admin.site.register(Answer, ValueAnswer)