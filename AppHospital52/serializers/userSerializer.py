from rest_framework import serializers
from AppHospital52.models.user import User
from AppHospital52.models.account import Account
from AppHospital52.serializers.accountSerializer import AccountSerializer

class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields = ['username', 'password', 'perfil', 'nombre', 'apellido', 'telefono', 'genero']

    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        return userInstance
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)
        return {
                'username': user.username,
                'password':user.password,
                'perfil':user.perfil,
                'nombre': user.nombre,
                'apellido': user.apellido,
                'telefono': user.telefono,
                'genero': user.genero,
                'account': {
                'id': account.id,
                'balance': account.balance,
                'lastChangeDate': account.lastChangeDate,
                'isActive': account.isActive
                }
        }