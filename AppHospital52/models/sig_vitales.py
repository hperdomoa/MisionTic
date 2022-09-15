from django.db import models
from .paciente import Paciente

class SignosVitales (models.Model):
    id_signos = models.AutoField(primary_key=True)
    oximetria = models.CharField('Oximetria', max_length=30)
    frecuenciaRes = models.CharField('FrecuenciaRes', max_length=30)
    frecuenciaCar = models.CharField('FrecuenciaCar', max_length=30)
    temperatura = models.CharField('Temperatura', max_length=30)
    glisemia = models.CharField('Glisemia', max_length=30)
    presionArt = models.CharField('PresionArt', max_length=30)
    fechahora = models.DateTimeField('Fechahora',max_length=30)
    id_paciente = models.ForeignKey(Paciente, related_name='sig_vitales', on_delete=models.CASCADE)