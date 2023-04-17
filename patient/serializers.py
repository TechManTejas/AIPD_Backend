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
        fields = ['user_data', 'condition_id', 'duration']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','first_name','last_name']


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = User
        fields = ['id', 'user']


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    doctor = DoctorSerializer()
    condition = ConditionSerializer()
    start_date = serializers.SerializerMethodField()
    end_date = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = '__all__'

    def get_start_date(self, obj):
        return obj.user.date_joined.strftime('%d/%m/%Y')

    def get_end_date(self, obj):
        from dateutil.relativedelta import relativedelta
        return (obj.user.date_joined + relativedelta(months=obj.duration)).strftime('%d/%m/%Y')
