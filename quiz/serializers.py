from django.db.models.base import Model
from rest_framework import serializers
from .models import Quiz

class Quizserializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'body', 'answer')