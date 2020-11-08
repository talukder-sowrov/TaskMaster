from django.contrib import admin
from .models import Person, Client

admin.site.register(Person)
admin.site.register(Client)