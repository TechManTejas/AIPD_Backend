from rest_framework import viewsets
from .models import FittlyfPhysio
from .serializers import FittlyfPhysioSerializer


class FittlyfPhysioViewSet(viewsets.ModelViewSet):
    queryset = FittlyfPhysio.objects.all()
    serializer_class = FittlyfPhysioSerializer
