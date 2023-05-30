from rest_framework import serializers
from .models import PatientExercise


class PatientExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientExercise
        fields = ['id', 'patient', 'exercise', 'sets', 'reps']
