from django.contrib import admin
from .models import *  # Importa os modelos do Models.py
# Modelos registados

admin.site.register(Products) # Regista o modelo Produto 
admin.site.register(User) # Regista o modelo User (se houver)
admin.site.register(StockProduct) # Regista o modelo StockProduct
admin.site.register(Modules) # Regista o modelo Modules
admin.site.register(Countries) # Regista o modelo Countries