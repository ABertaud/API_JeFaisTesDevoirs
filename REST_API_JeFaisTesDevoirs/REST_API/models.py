# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

import uuid

class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return str(self.id)

class Subject(models.Model):
    FileRef = models.ForeignKey(File, default=0, on_delete=models.CASCADE)
    Answered = models.BooleanField(default=False)
    UserRef = models.ForeignKey(User, on_delete=models.CASCADE)
    Price = models.IntegerField(default=0)
    hasPaid = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)

class Answer(models.Model):
    FileRef = models.ForeignKey(File, default=0, on_delete=models.CASCADE)
    SubjectRef = models.ForeignKey(Subject, on_delete=CASCADE)
    UserRef = models.ForeignKey(User, on_delete=models.CASCADE)
    isValid = models.BooleanField(default=False)
    isPending = models.BooleanField(default=True)
    isPaid = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)
