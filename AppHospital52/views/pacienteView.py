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


    def get_object(self, pk):
        try:
            return Paciente.objects.all(pk=pk)
        except Paciente.DoesNotExist:
            raise Http404
       
    



