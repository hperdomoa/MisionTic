from urllib import request
from rest_framework import status, views
from rest_framework.response import Response
from AppHospital52.serializers.ciudadSerializer import CiudadSerializer

class GestionCiudad(views.APIView):
    def post(self, request):
        serializer = CiudadSerializer (data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    



    #def get(self, request, *args, **kwargs):
        #token = request.META.get('HTTP_AUTHORIZATION')[7:]
        #tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        #valid_data = tokenBackend.decode(token,verify=False)

        #if valid_data['user_id'] != kwargs['pk']:
         #   stringResponse = {'detail':'Unauthorized Request'}
          #  return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

      #  return super().get(request, *args, **kwargs)