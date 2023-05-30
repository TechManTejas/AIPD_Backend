from django.shortcuts import render
from rest_framework import viewsets
from .models import PatientExercise
from .serializers import PatientExerciseSerializer


class PatientExerciseViewSet(viewsets.ModelViewSet):
    queryset = PatientExercise.objects.all()
    serializer_class = PatientExerciseSerializer

    def get_queryset(self):
        return PatientExercise.objects.filter(patient__user=self.request.user)
