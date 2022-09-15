from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response

from AppHospital52.serializers.ciudadSerializer import CiudadSerializer

class GestionCiudadId(generics.RetrieveAPIView):
    queryset = CiudadSerializer.objects.all()
    serializer_class = CiudadSerializer
    #permission_classes = (IsAuthenticated,)

   