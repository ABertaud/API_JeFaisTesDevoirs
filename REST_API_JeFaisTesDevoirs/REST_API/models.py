# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Subject(models.Model):
    #pdf... to fill and think about ... subject
    Answered = models.BooleanField(default=False)
    UserRef = models.ForeignKey(User, on_delete=models.CASCADE)
    Price = models.IntegerField(default=0)
    hasPaid = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)

class Answer(models.Model):
    #pdf to fill and think about ... answer
    SubjectRef = models.ForeignKey(Subject, on_delete=CASCADE)
    UserRef = models.ForeignKey(User, on_delete=models.CASCADE)
    isValid = models.BooleanField(default=False)
    isPending = models.BooleanField(default=True)
    isPaid = models.BooleanField(default=False)
