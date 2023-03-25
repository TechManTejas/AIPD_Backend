
from django.contrib.auth.models import User
from rest_framework import serializers
from patient.models import Patient
from condition.models import Condition

class PatientCreateSerializer(serializers.ModelSerializer):
    user_data = serializers.JSONField(required=True)

    class Meta:
        model = Patient
        fields = ['user_data', 'doctor_id', 'condition_id']


class PatientSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    doctor_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    condition_id = serializers.PrimaryKeyRelatedField(queryset=Condition.objects.all())

    class Meta:
        model = Patient
        fields = ['id', 'user', 'doctor_id', 'condition_id']
