from rest_framework import serializers
from .models import Condition
from exercise.serializers import ExerciseSerializer

class ConditionSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True)
    class Meta:
        model = Condition
        fields = [
            "id",
            "name",
            "exercises"
        ]