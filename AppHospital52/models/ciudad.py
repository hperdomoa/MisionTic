from django.db import models

class Ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    ciudad = models.CharField('ciudad', max_length = 15, unique=True)