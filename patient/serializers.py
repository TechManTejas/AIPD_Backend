
from django.contrib.auth.models import User
from rest_framework import serializers
from patient.models import Patient
from condition.models import Condition
from doctor.serializers import DoctorSerializer
from user.serializers import UserSerializer
from condition.serializers import ConditionSerializer

class PatientCreateSerializer(serializers.ModelSerializer):
    user_data = serializers.JSONField(required=True)

    class Meta:
        model = Patient
        fields = ['user_data', 'doctor_id', 'condition_id']


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    doctor = DoctorSerializer()
    condition = ConditionSerializer()

    class Meta:
        model = Patient
        fields = ['user', 'doctor', 'condition']
