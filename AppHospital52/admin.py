from django.contrib import admin
from .models.user import User
from .models.account import Perfil
from .models.ciudad import Ciudad
from .models.familiar import Familiar
from .models.paciente import Paciente
from .models.his_clinica import HistoriaClinica
from .models.sig_vitales import SignosVitales
from .models.per_salud import PersonalSalud

admin.site.register(User)
admin.site.register(Perfil)
admin.site.register(Ciudad)
admin.site.register(Familiar)
admin.site.register(Paciente)
admin.site.register(HistoriaClinica)
admin.site.register(SignosVitales)
admin.site.register(PersonalSalud)