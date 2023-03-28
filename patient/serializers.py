from rest_framework import serializers
from condition.serializers import ConditionSerializer
from patient.models import Patient
from django.contrib.auth.models import User
from doctor.models import Doctor


class PatientCreateSerializer(serializers.ModelSerializer):
    user_data = serializers.JSONField(required=True)
    condition_id = serializers.IntegerField(required=True)
    class Meta:
        model = Patient
        fields = ['user_data', 'condition_id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = User
        fields = ['id', 'user']


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    doctor = DoctorSerializer()
    condition = ConditionSerializer()
    class Meta:
        model = Patient
        fields = '__all__'
