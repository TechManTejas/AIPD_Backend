from rest_framework import viewsets
from .models import Doctor
from .serializers import DoctorSerializer

class ProductModelViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    http_method_names = ('get')
