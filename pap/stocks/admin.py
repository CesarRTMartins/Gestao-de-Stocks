from django.contrib import admin
from .models import *  # Importa os modelos do Models.py
# Modelos registados

admin.site.register(Products)  # Regista o modelo Produto 
admin.site.register(User)     # Regista o modelo User (se houver)
admin.site.register(StockProduct) # Regista o modelo stock_Product
