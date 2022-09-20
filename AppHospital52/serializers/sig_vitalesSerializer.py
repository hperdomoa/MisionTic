from rest_framework import serializers
from AppHospital52.models.sig_vitales import SignosVitales


class SignosVitalesSerializer (serializers.ModelSerializer):
    class Meta:
        model= SignosVitales
        fields=['id_signos','oximetria','frecuenciaRes','frecuenciaCar','temperatura','glisemia','presionArt','fechahora','id_paciente']
