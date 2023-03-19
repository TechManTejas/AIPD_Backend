from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token
from doctor.serializers import DoctorSerializer
from condition.serializers import ConditionSerializer

class UserSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    condition = ConditionSerializer()
    class Meta:
        model = User
        fields = ['id', 'doctor', 'condition', 'duration', 'username', 'phonenumber', 'code']