from urllib import request
from rest_framework import status, views
from rest_framework.response import Response
from AppHospital52.models import HistoriaClinica
from AppHospital52.serializers.his_clinicaSerializer import HistoriaClinicaSerializer

class GestionHisClinica(views.APIView):
    def post(self, request):
        serializer = HistoriaClinicaSerializer (data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
            serializer = HistoriaClinica.objects.all()
            serializerR = HistoriaClinicaSerializer(serializer, many=True)
            return Response(serializerR.data)