
from rest_framework import serializers
from company.serializers import CompanySerializer

from patient.serializers import PatientSerializer
from .models import Doctor
from patient.models import Patient
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    patients = PatientSerializer(many=True)
    company = CompanySerializer()
    class Meta:
        model = Doctor
        fields = '__all__'
