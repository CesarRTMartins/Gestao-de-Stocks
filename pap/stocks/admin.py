from django.contrib import admin
from .models.administration import *
from .models.common import * 
from .models.products import *
from .models.users import *
from .models.clients import * 
from .models.clients import *
from .models.orders import *
from .models.suppliers import *
# Modelos registados

admin.site.register(Products) # Regista o modelo Produto 
admin.site.register(User) # Regista o modelo User (se houver)
admin.site.register(StockProduct) # Regista o modelo StockProduct
admin.site.register(Modules) # Regista o modelo Modules
admin.site.register(Countries) # Regista o modelo Countries