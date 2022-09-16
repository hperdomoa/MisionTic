from AppHospital52.models.account import Perfil
from rest_framework import serializers

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ['id_perfil','nombre','isActive']