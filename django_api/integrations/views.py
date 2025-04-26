from rest_framework import viewsets
from .models import Inscripcion
from .serializers import InscripcionSerializer

class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all().order_by('-fecha_creacion')
    serializer_class = InscripcionSerializer
