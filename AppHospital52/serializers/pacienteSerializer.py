from rest_framework import serializers
from AppHospital52.models.paciente import Paciente


class PacienteSerializer (serializers.ModelSerializer):
    class Meta:
        model= Paciente
        field=['id_per_salud','username','id_ciudad','fecha_nacimiento','direccion']

