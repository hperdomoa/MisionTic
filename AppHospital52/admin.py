from django.contrib import admin
from .models.user import User
from .models.account import Perfil
from .models.ciudad import Ciudad


admin.site.register(User)
admin.site.register(Perfil)
admin.site.register(Ciudad)
