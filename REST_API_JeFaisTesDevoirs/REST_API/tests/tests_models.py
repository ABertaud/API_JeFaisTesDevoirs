from django.db.models.fields.files import FileField
from django.test import TestCase
from django.contrib.auth.models import User
from REST_API.models import File, Subject, Answer
from django.core.files.uploadedfile import SimpleUploadedFile

class JeFaisTesDevoirsModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='foobar',
            email='foo@bar.com',
            password='barbaz')
        self.file = File.objects.create(file="tmp")
        self.subject = Subject.objects.create(FileRef=self.file, Answered=False, UserRef=self.user, Price=15, hasPaid=False)
        self.answer = Answer.objects.create(FileRef=self.file, SubjectRef=self.subject, UserRef=self.user, isValid=True, isPending=False, isPaid=False)

    def testSubjectCreation(self):
        self.assertTrue(isinstance(self.subject, Subject))
        self.assertEqual(self.subject.__str__(), str(self.subject.id))
        self.assertEqual(self.subject.FileRef, self.file)
        self.assertEqual(self.subject.Answered, False)
        self.assertEqual(self.subject.UserRef, self.user)
        self.assertEqual(self.subject.Price, 15)
        self.assertEqual(self.subject.hasPaid, False)

    def testAnswerCreation(self):
        self.assertTrue(isinstance(self.answer, Answer))
        self.assertEqual(self.answer.__str__(), str(self.answer.id))
        self.assertEqual(self.answer.FileRef, self.file)
        self.assertEqual(self.answer.SubjectRef, self.subject)
        self.assertEqual(self.answer.UserRef, self.user)
        self.assertEqual(self.answer.isValid, True)
        self.assertEqual(self.answer.isPending, False)
        self.assertEqual(self.answer.isPaid, False)
    
    def testFileCreation(self):
        self.assertTrue(isinstance(self.file, File))
        self.assertEqual(self.file.__str__(), str(self.file.id))
        self.assertEqual(self.file.file, "tmp")