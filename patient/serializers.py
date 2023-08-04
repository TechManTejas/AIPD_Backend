from rest_framework import serializers
from datetime import date, datetime
from company.serializers import CompanySerializer
from condition.serializers import ConditionSerializer
from patient.models import Patient
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta

class PatientCreateSerializer(serializers.ModelSerializer):
    user_data = serializers.JSONField(required=True)
    condition_id = serializers.IntegerField(required=True)
    class Meta:
        model = Patient
        fields = ['user_data', 'condition_id', 'duration']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','first_name','last_name']


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    company = CompanySerializer()
    class Meta:
        model = User
        fields = ['id', 'user', 'company']


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    doctor = DoctorSerializer()
    condition = ConditionSerializer()
    start_date = serializers.SerializerMethodField()
    end_date = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = '__all__'

    def get_start_date(self, obj):
        return obj.user.date_joined.strftime('%d-%B-%Y')

    def get_end_date(self, obj):
        return (obj.user.date_joined + relativedelta(months=obj.duration)).strftime('%d-%B-%Y')
    
    def get_status(self, obj):
        end_date = obj.user.date_joined + relativedelta(months=obj.duration)
        end_date = end_date.date()
        today = date.today()
        return today <= end_date