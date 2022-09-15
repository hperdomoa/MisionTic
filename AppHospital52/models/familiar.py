from django.db import models
from .user import User
from .paciente import Paciente

class Familiar (models.Model):
    id_familiar = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, related_name='familiar', on_delete=models.CASCADE)
    id_paciente = models.ForeignKey(Paciente, related_name='familiar', on_delete=models.CASCADE)
    parentesco = models.CharField('Parentesco', max_length=30)
    correo = models.EmailField('Correo', max_length=100)