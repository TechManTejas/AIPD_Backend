from rest_framework import viewsets
from .models import ExerciseRecord
from .serializers import ExerciseRecordSerializer


class ExerciseRecordViewSet(viewsets.ModelViewSet):
    queryset = ExerciseRecord.objects.all()
    serializer_class = ExerciseRecordSerializer

    def get_queryset(self):
        return ExerciseRecord.objects.filter(patient__user=self.request.user)
