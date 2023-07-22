from rest_framework import viewsets
from .models import ExerciseRecord
from .serializers import ExerciseRecordSerializer


class ExerciseRecordViewSet(viewsets.ModelViewSet):
    queryset = ExerciseRecord.objects.all()
    serializer_class = ExerciseRecordSerializer
    
    def get_queryset(self):
        if hasattr(self.request.user, 'patient'):
            return ExerciseRecord.objects.filter(patient__user=self.request.user)
        elif hasattr(self.request.user, 'fittlyf_physio'):
            return ExerciseRecord.objects.filter(patient__user__id=self.request.data.patient_id)
