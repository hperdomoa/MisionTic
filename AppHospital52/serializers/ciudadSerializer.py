from rest_framework import serializers
from AppHospital52.models.ciudad import Ciudad

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ['ciudad']


