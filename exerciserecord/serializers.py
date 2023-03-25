from rest_framework import serializers
from .models import ExerciseRecord


class ExerciseRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseRecord
        fields = ['id', 'patient', 'exercise', 'date']
