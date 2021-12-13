from django.test import TestCase
from django.contrib.auth.models import User
from REST_API.models import Subject, Answer

class JeFaisTesDevoirsModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='foobar',
            email='foo@bar.com',
            password='barbaz')
        self.subject = Subject.objects.create(File="test.zip", Answered=False, UserRef=self.user, Price=15, hasPaid=False)
        self.answer = Answer.objects.create(File="answer.zip", SubjectRef=self.subject, UserRef=self.user, isValid=True, isPending=False, isPaid=False)

    def testSubjectCreation(self):
        self.assertTrue(isinstance(self.subject, Subject))
        self.assertEqual(self.subject.__str__(), str(self.subject.id))
        self.assertEqual(self.subject.File, "test.zip")
        self.assertEqual(self.subject.Answered, False)
        self.assertEqual(self.subject.UserRef, self.user)
        self.assertEqual(self.subject.Price, 15)
        self.assertEqual(self.subject.hasPaid, False)

    def testAnswerCreation(self):
        self.assertTrue(isinstance(self.answer, Answer))
        self.assertEqual(self.answer.__str__(), str(self.answer.id))
        self.assertEqual(self.answer.File, "answer.zip")
        self.assertEqual(self.answer.SubjectRef, self.subject)
        self.assertEqual(self.answer.UserRef, self.user)
        self.assertEqual(self.answer.isValid, True)
        self.assertEqual(self.answer.isPending, False)
        self.assertEqual(self.answer.isPaid, False)