from rest_framework import serializers
from AppHospital52.models.per_salud import PersonalSalud


class PersonalSaludSerializer (serializers.ModelSerializer):
    class Meta:
        model= PersonalSalud
        field=['username','rol','especialidad']

