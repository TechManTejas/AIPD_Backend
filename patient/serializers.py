from rest_framework import serializers
from .models import Patient
from doctor.serializers import DoctorSerializer
from condition.serializers import ConditionSerializer

class PatientSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    condition = ConditionSerializer()
    class Meta:
        model = Patient
        fields = [
            "id",
            "name",
            "phone_no",
            "code",
            "doctor",
            "condition"
        ]
