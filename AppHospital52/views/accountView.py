from urllib import request
from rest_framework import status, views
from rest_framework.response import Response
from AppHospital52.models import Perfil
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