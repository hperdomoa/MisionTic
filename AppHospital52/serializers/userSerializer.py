from rest_framework import serializers
from AppHospital52.models.user import User
from AppHospital52.models.account import Perfil
#from AppHospital52.serializers.accountSerializer import PerfilSerializer

class UserSerializer(serializers.ModelSerializer):
    #account = PerfilSerializer()
    class Meta:
        model = User
        fields = ['id','username', 'password', 'nombre', 'apellido', 'telefono', 'genero','id_perfil']

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        Perfil.objects.create(user=userInstance)
        return userInstance



    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        account = Perfil.objects.get(user=obj.id)
        return {
                'id':user.id,
                'username': user.username,
                'password':user.password,
                'id_perfil':user.id_perfil,
                'nombre': user.nombre,
                'apellido': user.apellido,
                'telefono': user.telefono,
                'genero': user.genero,
                'account': {
                'id_perfil': account.id_perfil,
                'nombre': account.nombre,
                'isActive': account.isActive,
                }
                
        }


   