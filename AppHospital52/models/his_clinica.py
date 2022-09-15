from django.db import models
from .paciente import Paciente

class HistoriaClinica (models.Model):
    id_historiaclinica = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, related_name='his_clinica', on_delete=models.CASCADE)
    sugenrencias = models.CharField('Sugenrencias',max_length=250)
    diagnostico = models.CharField('Diagnostico',max_length=250)
    entorno = models.CharField('Entorno',max_length=250)
    fechasugerencias = models.DateField('Fechasugerencias',max_length=250)
    descripcion= models.CharField('Descripcion', max_length=250)