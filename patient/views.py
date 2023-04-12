from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from doctor.models import Doctor
from .models import Patient
from .serializers import PatientSerializer, PatientCreateSerializer
import random
import string

def generate_random_sequence():
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

    sequence = ''.join(
        [random.choice(string.ascii_lowercase),random.choice(string.ascii_uppercase),random.choice(string.digits)] 
        +
        [random.choice(chars) for _ in range(3)]
    )

    sequence = ''.join(random.sample(sequence, len(sequence)))

    return sequence

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_queryset(self):
        if hasattr(self.request.user, 'patient'):
            return Patient.objects.filter(user=self.request.user.id)
        elif hasattr(self.request.user, 'doctor'):
            return Patient.objects.filter(doctor__user__id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        if hasattr(self.request.user, 'doctor'):
            serializer = PatientCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user_data = serializer.validated_data.pop('user_data')
            condition_id = serializer.validated_data.pop('condition_id')
            doctor_id = self.request.user.doctor.id

            # Create a new user object
            password = generate_random_sequence()
            user_data['password'] = password
            user = User.objects.create_user(**user_data)

            # Create a new patient object
            patient = Patient.objects.create(user=user, doctor_id=doctor_id,condition_id=condition_id)

            # Create a new token object
            token, created = Token.objects.get_or_create(user=user)

            serializer = self.get_serializer(patient)
            headers = self.get_success_headers(serializer.data)

            return Response({'code': password}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'message': 'Only doctors can create patients'}, status=status.HTTP_403_FORBIDDEN)
