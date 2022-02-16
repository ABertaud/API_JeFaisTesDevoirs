from rest_framework.test import APIRequestFactory, force_authenticate
from django.test import TestCase
from REST_API.models import CustomUser, Answer, File, Subject
from REST_API.views import CustomUserViewSet, FileViewSet, SubjectViewSet, AnswerViewSet
from django.core.files.base import ContentFile


class ViewSetTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_superuser(
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

    def testRemoveFileFromSubjectID(self):
        request_url = f'Subject/remove_file_from_subjectid/'
        view = SubjectViewSet.as_view(actions={'get': 'remove_file_from_subjectid'})
        request = self.factory.get(request_url, {'id_subject': 15})
        response = view(request)
        self.assertEqual(response.status_code, 401)
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, 400)
        request = self.factory.get(request_url, {'id_subject': 1})
        force_authenticate(request, user=self.user)
        response = view(request)
        #no file created results in fail
        self.assertEqual(response.status_code, 400)
    
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
    
    def testRemoveFileFromAnswerID(self):
        request_url = f'Answer/remove_file_from_answerid/'
        view = AnswerViewSet.as_view(actions={'get': 'remove_file_from_answerid'})
        request = self.factory.get(request_url, {'id_answer': 15})
        response = view(request)
        self.assertEqual(response.status_code, 401)
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, 400)
        request = self.factory.get(request_url, {'id_answer': 1})
        force_authenticate(request, user=self.user)
        response = view(request)
        #no file created results in fail
        self.assertEqual(response.status_code, 400)

    def test_CustomUserViewSet(self):
        view = CustomUserViewSet.as_view({'get': 'retrieve'})
        request = self.factory.get('CustomUser')
        response = view(request, pk=self.user.pk)
        self.assertEqual(response.status_code, 401)
        force_authenticate(request, user=self.user)
        response = view(request, pk=10)
        self.assertEqual(response.status_code, 404)
        response = view(request, pk=self.user.pk)
        self.assertEqual(response.status_code, 200)