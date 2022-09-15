from django.db import models
from .user import User


class PersonalSalud (models.Model):
    id_per_salud = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, related_name='per_salud', on_delete=models.CASCADE)
    rol = models.CharField('Rol',max_length=30)
    especialidad= models.CharField('Especialidad', max_length=30)