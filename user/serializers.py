from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from patient.models import Patient
from doctor.models import Doctor

class UserSerializer(serializers.ModelSerializer):
    # details = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # def get_details(self, obj):
    #     if hasattr(obj, 'patient'):
    #         serializer = PatientUserSerializer(obj.patient)
    #     elif hasattr(obj, 'doctor'):
    #         serializer = DoctorUserSerializer(obj.doctor)
    #     else:
    #         serializer = None

    #     return serializer.data if serializer else {}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        token = Token.objects.create(user=user)
        return {'user': user, 'token': token.key}
    
# class PatientUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Patient
#         fields = '__all__'


# class DoctorUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Doctor
#         fields ='__all__'
