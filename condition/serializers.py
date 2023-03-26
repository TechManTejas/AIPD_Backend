
from rest_framework import serializers
from .models import Condition
from exercise.serializers import ExerciseSerializer
from user.serializers import UserSerializer
from patient.models import Patient

class ConditionSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)
    class Meta:
        model = Condition
        fields = ['id', 'name', 'exercises']
