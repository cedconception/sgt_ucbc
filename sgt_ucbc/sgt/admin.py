from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Etudiant)
admin.site.register(SujetDeposer)
admin.site.register(Memoire)
admin.site.register(Diffusion)
admin.site.register(Director)
admin.site.register(Encadreur)
admin.site.register(Departement)
admin.site.register(Faculty)
