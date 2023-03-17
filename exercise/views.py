from rest_framework import viewsets
from .models import Exercise
from .serializers import ExerciseSerializer


class ProductModelViewset(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    http_method_names = ('get')
