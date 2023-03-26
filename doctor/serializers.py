
from rest_framework import serializers
from .models import Doctor
from patient.models import Patient
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']


class PatientsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Patient
        fields = ['id','user']


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    patients = PatientsSerializer(many=True)
    class Meta:
        model = Doctor
        fields = '__all__'
