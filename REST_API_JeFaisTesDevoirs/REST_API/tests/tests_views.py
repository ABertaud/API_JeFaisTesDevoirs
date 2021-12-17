from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth.models import User
from django.test import TestCase
from REST_API.models import Answer, File, Subject
from REST_API.views import FileViewSet, SubjectViewSet, AnswerViewSet
from django.core.files.base import ContentFile


class ViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='foobar',
            email='foo@bar.com',
            password='barbaz')
        tmp_file = ContentFile('text', 'name')
        self.file = File.objects.create(file="tmp")
        self.subject = Subject.objects.create(FileRef=self.file, Answered=False, UserRef=self.user, Price=15, hasPaid=False)
        self.answer = Answer.objects.create(FileRef=self.file, SubjectRef=self.subject, UserRef=self.user, isValid=True, isPending=False, isPaid=False)
        self.factory  = APIRequestFactory()
    
    def testSubjectViewSet(self):
        view = SubjectViewSet.as_view({'get': 'retrieve'})
        request = self.factory.get('Subject')
        response = view(request, pk=self.subject.pk)
        self.assertEqual(response.status_code, 401)
        force_authenticate(request, user=self.user)
        response = view(request, pk=10)
        self.assertEqual(response.status_code, 404)
        response = view(request, pk=self.subject.pk)
        self.assertEqual(response.status_code, 200)
    
    def testAnswerViewSet(self):
        view = AnswerViewSet.as_view({'get': 'retrieve'})
        request = self.factory.get('Answer')
        response = view(request, pk=self.answer.pk)
        self.assertEqual(response.status_code, 401)
        force_authenticate(request, user=self.user)
        response = view(request, pk=10)
        self.assertEqual(response.status_code, 404)
        response = view(request, pk=self.answer.pk)
        self.assertEqual(response.status_code, 200)
    
    def testFileViewSet(self):
        view = FileViewSet.as_view({'get': 'retrieve'})
        request = self.factory.get('File')
        response = view(request, pk=self.file.pk)
        self.assertEqual(response.status_code, 401)
        force_authenticate(request, user=self.user)
        response = view(request, pk=10)
        self.assertEqual(response.status_code, 404)
        response = view(request, pk=self.file.pk)
        self.assertEqual(response.status_code, 200)