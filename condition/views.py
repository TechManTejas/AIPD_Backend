from rest_framework import viewsets
from .models import Condition
from .serializers import ConditionSerializer


class ConditionModelViewset(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    http_method_names = ('get')
