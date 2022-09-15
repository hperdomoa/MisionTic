from django.contrib import admin
from .models.user import User
from .models.account import Account
from .models.ciudad import Ciudad


admin.site.register(User)
admin.site.register(Account)
admin.site.register(Ciudad)