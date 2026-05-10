from django.contrib import admin

# Register your models here.
#importer le model creer ici, avec * importer tous les models creer
from .models import *

#on autorise l'administrateur a pouvoir modifier, faire un CRUD sur Employe
admin.site.register(Employe)


