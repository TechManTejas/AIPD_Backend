
from rest_framework import serializers
from .models import Doctor
from user.serializers import UserSerializer
from patient.models import Patient
from condition.serializers import ConditionSerializer


class DoctorPatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    condition = ConditionSerializer()
    class Meta:
        model = Patient
        fields = ['id', 'user', 'condition']


class DoctorUserSerializer(serializers.ModelSerializer):
    patients = DoctorPatientSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ['patients']

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    patients = DoctorPatientSerializer(many=True, read_only=True)
    class Meta:
        model = Doctor
        fields = ['user','patients']
