from django.shortcuts import render
from rest_framework import viewsets
from .models import PatientExercise
from .serializers import PatientExerciseSerializer


class PatientExerciseViewSet(viewsets.ModelViewSet):
    queryset = PatientExercise.objects.all()
    serializer_class = PatientExerciseSerializer

    def get_queryset(self):
        if hasattr(self.request.user, 'patient'):
            return PatientExercise.objects.filter(patient__user=self.request.user)
        elif hasattr(self.request.user, 'fittlyf_physio'):
            patient_id = self.request.query_params.get('patient_id')
            if patient_id:
                return PatientExercise.objects.filter(patient__id=patient_id)
