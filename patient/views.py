from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer


class ProductModelViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    http_method_names = ('get')
