from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ExerciseRecord
from .serializers import ExerciseRecordSerializer


class ExerciseRecordViewSet(viewsets.ModelViewSet):
    queryset = ExerciseRecord.objects.all()
    serializer_class = ExerciseRecordSerializer
    
    def get_queryset(self):
        if hasattr(self.request.user, 'patient'):
            return ExerciseRecord.objects.filter(patient__user=self.request.user)
        elif hasattr(self.request.user, 'fittlyf_physio'):
            patient_id = self.request.query_params.get('patient_id')
            exercise_record_id = self.request.query_params.get('exercise_record_id')

            if patient_id:
                return ExerciseRecord.objects.filter(patient__id=patient_id)
            if exercise_record_id:
                return ExerciseRecord.objects.filter(id=exercise_record_id)
            
class RedundantExerciseRecordViewSet(viewsets.ModelViewSet):
    queryset = ExerciseRecord.objects.all()
    serializer_class = ExerciseRecordSerializer