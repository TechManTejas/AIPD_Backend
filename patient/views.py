from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer, PatientCreateSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def create(self, request, *args, **kwargs):
        serializer = PatientCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.validated_data.pop('user_data')
        doctor_id = serializer.validated_data.pop('doctor_id')
        condition_id = serializer.validated_data.pop('condition_id')

        # Create a new user object
        user = User(**user_data)
        user.save()

        # Create a new patient object
        patient = Patient(user=user, doctor_id=doctor_id, condition_id=condition_id)
        patient.save()

        serializer = self.get_serializer(patient)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
