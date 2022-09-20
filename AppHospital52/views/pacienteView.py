from urllib import request
from AppHospital52.models import Paciente
from rest_framework import status, views
from rest_framework.response import Response
from django.http import Http404
from AppHospital52.serializers.pacienteSerializer import PacienteSerializer

class GestionPaciente(views.APIView):
    def post(self, request):
        serializer = PacienteSerializer (data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        serializer = Paciente.objects.all()
        serializerR = PacienteSerializer(serializer, many=True)
        return Response(serializerR.data)

class GestionDetailPaciente(views.APIView):
    
    '''Consulta Errada'''
    def get_object(self, pk):
        try:
            return Paciente.objects.get(pk=pk)
        except Paciente.DoesNotExist:
            raise Http404
    '''Consulta Por Id Valida'''
    def get(self, request, pk, format=None):
        Paciente = self.get_object(pk)
        serializer = PacienteSerializer(Paciente)
        return Response(serializer.data)
    '''Actualizar por Id'''
    def put(self, request, pk, format=None):
        Paciente = self.get_object(pk)
        serializer = PacienteSerializer(Paciente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''Borrar por Id'''
    def delete(self, request, pk, format=None):
        Paciente = self.get_object(pk)
        Paciente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
       
    



