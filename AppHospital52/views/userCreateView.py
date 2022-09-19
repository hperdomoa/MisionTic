from rest_framework import status, views
from rest_framework.response import Response
from AppHospital52.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from AppHospital52.serializers.userSerializer import UserSerializer

class UserCreateView(views.APIView):
        def post(self, request, *args, **kwargs):
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            tokenData = {"username":request.data["username"],
                         "password":request.data["password"]}
            tokenSerializer = TokenObtainPairSerializer(data=tokenData)
            tokenSerializer.is_valid(raise_exception=True)
            return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)


        def get(self, request, format=None):
            serializer = User.objects.all()
            serializerR = UserSerializer(serializer, many=True)
            return Response(serializerR.data)