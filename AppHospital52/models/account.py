from django.db import models

class Perfil(models.Model):
    id_perfil = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length = 30)
    isActive = models.BooleanField(default=True)