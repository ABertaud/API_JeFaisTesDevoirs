from rest_framework import serializers
from REST_API.models import Subject, Answer

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        depth = 1
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        depth = 1
        fields = '__all__'