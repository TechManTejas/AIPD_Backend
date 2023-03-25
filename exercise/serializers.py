from rest_framework import serializers
from .models import Exercise
from condition.models import Condition
from user.serializers import UserSerializer

class ExerciseConditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Condition
        fields = ['id', 'name']

class ExerciseSerializer(serializers.ModelSerializer):
    conditions = ExerciseConditionSerializer(many=True, read_only=True)
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'image','conditions']
