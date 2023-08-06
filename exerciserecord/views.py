from patient.models import Patient
from patient_exercise.models import PatientExercise
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ExerciseRecord
from .serializers import ExerciseRecordSerializer
from datetime import date

class ExerciseRecordViewSet(viewsets.ModelViewSet):
    queryset = ExerciseRecord.objects.all()
    serializer_class = ExerciseRecordSerializer

    def get_queryset(self):
        if hasattr(self.request.user, "patient"):
            return ExerciseRecord.objects.filter(patient__user=self.request.user)
        elif hasattr(self.request.user, "fittlyf_physio"):
            patient_id = self.request.query_params.get("patient_id")
            exercise_record_id = self.request.query_params.get("exercise_record_id")

            if patient_id:
                return ExerciseRecord.objects.filter(patient__id=patient_id)
            if exercise_record_id:
                return ExerciseRecord.objects.filter(id=exercise_record_id)

    def perform_create(self, request, *args, **kwargs):
        patient_exercises_ids = [
            patient_exercise.exercise.id
            for patient_exercise in PatientExercise.objects.filter(
                patient=request.data["patient"]
            )
        ]

        today_completed_exercise_ids = [
            exercise_record.exercise.id
            for exercise_record in ExerciseRecord.objects.filter(
                date=request.data["date"], patient=request.data["patient"]
            )
        ]

        completed_all_exercises = set(patient_exercises_ids) == set(
            today_completed_exercise_ids
        )
        if completed_all_exercises:
            patient_id = request.data["patient"]
            patient = Patient.objects.get(pk=patient_id)
            patient.completed_exercise_date = date.today()
            patient.save()

        serializer = ExerciseRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RedundantExerciseRecordViewSet(viewsets.ModelViewSet):
    queryset = ExerciseRecord.objects.all()
    serializer_class = ExerciseRecordSerializer
