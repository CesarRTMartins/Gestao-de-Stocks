from django.contrib import admin
from .models import Products, User  # Importa os modelos do Models.py
# Modelos registados

admin.site.register(Products)  # Registra o modelo Produto 
admin.site.register(User)     # Registra o modelo User (se houver)
