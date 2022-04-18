# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models.query import QuerySet
import os

from django.shortcuts import render
from rest_framework.fields import NullBooleanField
from REST_API.models import CustomUser, File, Subject, Answer
from REST_API.serializers import CustomUserSerializer, FileSerializer, SubjectSerializer, AnswerSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

class CustomUserViewSet(viewsets.ModelViewSet):
    """
    A simple viewset to retrieve all the Users
    """
    # permission_classes = (IsAuthenticated,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        return super(CustomUserViewSet, self).get_permissions()

class FileViewSet(viewsets.ModelViewSet):
    """
    A simple viewset to retrieve all the Files
    """
    permission_classes = (IsAuthenticated,)
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = self.serializer_class(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubjectViewSet(viewsets.ModelViewSet):
    """
    A simple viewset to retrieve all the Subjects
    """
    permission_classes = (IsAuthenticated,)
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
    @action(detail=False, methods=['GET'], name='Remove File From SubjectID')
    def remove_file_from_subjectid(self, request, pk=None):
        subject_id = request.GET.get("id_subject")
        if not id:
            return Response("No id_subject in the request.", status=400)
        subject_obj = self.queryset.filter(id=subject_id)
        if not subject_obj:
            return Response("No existant subject with the given id.", status=400)
        subject_obj = subject_obj.first()
        if subject_obj.FileRef.file:
            print(subject_obj.FileRef.file.path)
            if os.path.isfile(subject_obj.FileRef.file.path):
                os.remove(subject_obj.FileRef.file.path)
                subject_obj.FileRef.delete()
            else:
                return Response("It seems that the file you're willing to delete doesn't exist.", status=400)
        return Response({"The file has been removed."}, status=200)

class AnswerViewSet(viewsets.ModelViewSet):
    """
    A simple viewset to retrieve all the Answers
    """
    permission_classes = (IsAuthenticated,)
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    @action(detail=False, methods=['GET'], name='Remove File From AnswerID')
    def remove_file_from_answerid(self, request, pk=None):
        answer_id = request.GET.get("id_answer")
        if not id:
            return Response("No id_answer in the request.", status=400)
        answer_obj = self.queryset.filter(id=answer_id)
        if not answer_obj:
            return Response("No existant answer with the given id.", status=400)
        answer_obj = answer_obj.first()
        if answer_obj.FileRef.file:
            if os.path.isfile(answer_obj.FileRef.file.path):
                os.remove(answer_obj.FileRef.file.path)
                answer_obj.FileRef.delete()
            else:
                return Response("It seems that the file you're willing to delete doesn't exist.", status=400)
        return Response({"The file has been removed."}, status=200)
