from urllib import request
from rest_framework import status, views
from rest_framework.response import Response
from AppHospital52.models import SignosVitales
from django.http import Http404
from AppHospital52.serializers.sig_vitalesSerializer import SignosVitalesSerializer

class GestionSignosVitales(views.APIView):
    def post(self, request):
        serializer = SignosVitalesSerializer (data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
            serializer = SignosVitales.objects.all()
            serializerR = SignosVitalesSerializer(serializer, many=True)
            return Response(serializerR.data)


class GestionDetailSignosVitales(views.APIView):
    '''Consulta Errada'''
    def get_object(self, pk):
        try:
            return SignosVitales.objects.get(pk=pk)
        except SignosVitales.DoesNotExist:
            raise Http404
    '''Consulta Por Id Valida'''
    def get(self, request, pk, format=None):
        SignosVitales = self.get_object(pk)
        serializer = SignosVitalesSerializer(SignosVitales)
        return Response(serializer.data)
    '''Actualizar por Id'''
    def put(self, request, pk, format=None):
        SignosVitales = self.get_object(pk)
        serializer = SignosVitalesSerializer(SignosVitales, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''Borrar por Id'''
    def delete(self, request, pk, format=None):
        SignosVitales = self.get_object(pk)
        SignosVitales.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)