from urllib import request
from rest_framework import status, views
from rest_framework.response import Response
from AppHospital52.models import Perfil
from django.http import Http404
from AppHospital52.serializers.accountSerializer import PerfilSerializer

class GestionPerfil(views.APIView):
    def post(self, request):
        serializer = PerfilSerializer (data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
            serializer = Perfil.objects.all()
            serializerR = PerfilSerializer(serializer, many=True)
            return Response(serializerR.data)



class GestionDetailPerfil(views.APIView):
    
    '''Consulta Errada'''
    
    def get_object(self, pk):
        try:
            return Perfil.objects.get(pk=pk)
        except Perfil.DoesNotExist:
            raise Http404
    '''Consulta Por Id Valida'''
    def get(self, request, pk, format=None):
        Perfil = self.get_object(pk)
        serializer = PerfilSerializer(Perfil)
        return Response(serializer.data)
    '''Actualizar por Id'''
    def put(self, request, pk, format=None):
        Perfil = self.get_object(pk)
        serializer = PerfilSerializer(Perfil, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''Borrar por Id'''
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)