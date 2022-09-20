from rest_framework import serializers
from AppHospital52.models.his_clinica import HistoriaClinica

class HistoriaClinicaSerializer (serializers.ModelSerializer):
    class Meta:
        model= HistoriaClinica
        fields=['id_historiaclinica','id_paciente','sugenrencias','diagnostico','entorno','fechasugerencias','descripcion' ]

