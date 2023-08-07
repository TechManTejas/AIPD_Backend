from django.contrib.auth.models import User
from django.db.models import (
    F,
    ExpressionWrapper,
    IntegerField
)
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from datetime import date, timedelta
from .models import Patient
from .serializers import PatientSerializer, PatientCreateSerializer
import random
import string


def generate_random_sequence():
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

    sequence = "".join(
        [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
        ]
        + [random.choice(chars) for _ in range(3)]
    )

    sequence = "".join(random.sample(sequence, len(sequence)))

    return sequence


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_queryset(self):
        if hasattr(self.request.user, "patient"):
            return Patient.objects.filter(user=self.request.user.id)
        elif hasattr(self.request.user, "doctor"):
            return Patient.objects.filter(doctor__user__id=self.request.user.id)
        elif hasattr(self.request.user, "fittlyf_physio"):
            patient_id = self.request.query_params.get("patient_id")
            if patient_id:
                return Patient.objects.filter(id=patient_id)
            return Patient.objects.filter(fittlyf_physio__user__id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        if hasattr(self.request.user, "doctor"):
            serializer = PatientCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user_data = serializer.validated_data.pop("user_data")
            condition_id = serializer.validated_data.pop("condition_id")
            duration = serializer.validated_data.pop("duration")
            doctor_id = self.request.user.doctor.id

            # Create a new user object
            # password = generate_random_sequence()
            user_data["password"] = user_data["username"]
            user = User.objects.create_user(**user_data)

            # Calculate the default prompt_review value (2 days after user's date joined)
            prompt_review_default = user.date_joined + timedelta(days=2)

            # Create a new patient object
            patient = Patient.objects.create(
                user=user,
                doctor_id=doctor_id,
                condition_id=condition_id,
                duration=duration,
                prompt_review=prompt_review_default,
            )

            # Create a new token object
            token, created = Token.objects.get_or_create(user=user)

            # Get the ID of the created patient
            patient_id = patient.id

            serializer = self.get_serializer(patient)
            headers = self.get_success_headers(serializer.data)

            return Response(
                {"code": user_data["username"], "patient_id": patient_id},
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
        else:
            return Response(
                {"message": "Only doctors can create patients"},
                status=status.HTTP_403_FORBIDDEN,
            )


class ActivePatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer

    def get_queryset(self):
        today = date.today()

        queryset = Patient.objects.annotate(
            duration_days=ExpressionWrapper(
                F("duration") * 30, output_field=IntegerField()
            )
        )

        custom_queryset = []

        for patient in queryset:
            if patient.user.date_joined.date() > today - timedelta(
                days=patient.duration_days
            ):
                custom_queryset.append(patient)

        return custom_queryset
