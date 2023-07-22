
from rest_framework import serializers
from patient.serializers import PatientSerializer
from .models import FittlyfPhysio
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']


class FittlyfPhysioSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    patients = PatientSerializer(many=True)
    class Meta:
        model = FittlyfPhysio
        fields = '__all__'
