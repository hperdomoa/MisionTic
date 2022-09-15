from django.db import models
from .ciudad import Ciudad
from .user import User
from .per_salud import PersonalSalud

class Paciente (models.Model):
    id_paciente =  models.AutoField(primary_key=True)
    id_per_salud = models.ForeignKey(PersonalSalud, related_name='paciente', on_delete=models.CASCADE)
    username = models.ForeignKey(User, related_name='paciente', on_delete=models.CASCADE)
    id_ciudad = models.ForeignKey(Ciudad, related_name='paciente', on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField('Fecha_nacimiento',max_length=30)
    direccion= models.CharField('Direccion', max_length=100)