# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from REST_API.models import Subject, Answer
from REST_API.serializers import SubjectSerializer, AnswerSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class SubjectViewSet(viewsets.ModelViewSet):
    """
    A simple viewset to retrieve all the Subjects
    """
    permission_classes = (IsAuthenticated,)
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    """
    A simple viewset to retrieve all the Answers
    """
    permission_classes = (IsAuthenticated,)
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
