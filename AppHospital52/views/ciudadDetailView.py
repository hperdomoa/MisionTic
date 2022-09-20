from urllib import request
from rest_framework import status, views
from rest_framework.response import Response
from AppHospital52.models import Ciudad
from django.http import Http404
from AppHospital52.serializers.ciudadSerializer import CiudadSerializer

class GestionCiudad(views.APIView):
    def post(self, request):
        serializer = CiudadSerializer (data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        serializer = Ciudad.objects.all()
        serializerR = CiudadSerializer(serializer, many=True)
        return Response(serializerR.data)


class GestionDetailCiudad(views.APIView):
    
    '''Consulta Errada'''
    
    def get_object(self, pk):
        try:
            return Ciudad.objects.get(pk=pk)
        except Ciudad.DoesNotExist:
            raise Http404
    '''Consulta Por Id Valida'''
    def get(self, request, pk, format=None):
        Ciudad = self.get_object(pk)
        serializer = CiudadSerializer(Ciudad)
        return Response(serializer.data)
    '''Actualizar por Id'''
    def put(self, request, pk, format=None):
        Ciudad = self.get_object(pk)
        serializer = CiudadSerializer(Ciudad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''Borrar por Id'''
    def delete(self, request, pk, format=None):
        Ciudad = self.get_object(pk)
        Ciudad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
