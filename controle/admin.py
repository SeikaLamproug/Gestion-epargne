from django.contrib import admin

from accounts.models import Client, Profile, Agent, Payement, Compte
from .models import UserProfile
# Register your models here.
admin.site.register(UserProfile)


admin.site.register(Profile)
admin.site.register(Client)
admin.site.register(Agent)
admin.site.register(Payement)
admin.site.register(Compte)

