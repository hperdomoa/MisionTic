from urllib import request
from rest_framework import status, views
from rest_framework.response import Response
from AppHospital52.models import HistoriaClinica
from django.http import Http404
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


class GestionDetailHisClinica(views.APIView):
    '''Consulta Errada'''
    def get_object(self, pk):
        try:
            return HistoriaClinica.objects.get(pk=pk)
        except HistoriaClinica.DoesNotExist:
            raise Http404
    '''Consulta Por Id Valida'''
    def get(self, request, pk, format=None):
        HistoriaClinica = self.get_object(pk)
        serializer = HistoriaClinicaSerializer(HistoriaClinica)
        return Response(serializer.data)
    '''Actualizar por Id'''
    def put(self, request, pk, format=None):
        HistoriaClinica = self.get_object(pk)
        serializer = HistoriaClinicaSerializer(HistoriaClinica, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''Borrar por Id'''
    def delete(self, request, pk, format=None):
        HistoriaClinica = self.get_object(pk)
        HistoriaClinica.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)