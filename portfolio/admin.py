# Agregar modelo al sistema administrador de django
from django.contrib import admin
from .models import Project

admin.site.register(Project)
