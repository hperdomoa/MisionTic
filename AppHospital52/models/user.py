from django.db import models
from .account import Perfil
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Deben tener nombre de User')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
        username=username,
        password=password,
        

        )
        #user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(primary_key=True, max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256)
    nombre = models.CharField('Nombre', max_length = 30)
    apellido = models.CharField('Apellido', max_length = 30)
    telefono = models.CharField('Telefono', max_length = 30)
    genero = models.CharField('Genero', max_length = 30)
    id_perfil = models.ForeignKey(Perfil, related_name='account', on_delete=models.CASCADE)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
        
    objects = UserManager()
    USERNAME_FIELD = 'username'