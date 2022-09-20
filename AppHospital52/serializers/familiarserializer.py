from rest_framework import serializers
from AppHospital52.models.familiar import Familiar


class FamiliarSerializer (serializers.ModelSerializer):
    class Meta:
        model= Familiar
        field=['id_familiar','username','id_paciente','parentesco','correo' ]

