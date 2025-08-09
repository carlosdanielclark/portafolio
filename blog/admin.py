# Agregar modelo al sistema administrador de django
from django.contrib import admin
from .models import Post

admin.site.register(Post)
