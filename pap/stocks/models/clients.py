from django.db import models
from .common import Countries

class ClientCategory(models.Model):
    # Atributos da tabela
    name = models.CharField(max_length=200) # Nome da Categoria
    creation_date = models.DateTimeField(auto_now_add=True) # Data de criação da categoria
    update_date = models.DateTimeField(auto_now=True) # Data de atualização da categoria
    
    class Meta:
        db_table = 'client_category'  # Definindo o nome personalizado da tabela

class ClientType(models.Model):
    # Chave estrangeira (Trocar para Not Null IMPORTANTE)
    category = models.ForeignKey(ClientCategory, on_delete=models.CASCADE,null=True,db_column='client_category_id')
    # Atributos da tabela
    name = models.CharField(max_length=200) # Nome da Categoria
    creation_date = models.DateTimeField(auto_now_add=True) # Data de criação da categoria
    update_date = models.DateTimeField(auto_now=True) # Data de atualização da categoria

    class Meta:
        db_table = 'client_type'  # Definindo o nome personalizado da tabela

class Client(models.Model):
    # Chaves estrangeira
    clienttype = models.ForeignKey(ClientType, on_delete=models.CASCADE,db_column='client_type_id')
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, db_column='country_id')
    # Atributos da tabela
    active = models.PositiveSmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1)  # Activo ou não
    nif = models.CharField(max_length=12) # NIF
    name = models.CharField(max_length=200) # Nome da Categoria
    contact = models.CharField(max_length=200) # Contacto
    email = models.CharField(max_length=200) # Email
    password = models.CharField(max_length=200) # Password
    creation_date = models.DateTimeField(auto_now_add=True) # Data de criação da conta do Administrator
    update_date = models.DateTimeField(auto_now=True) # Data de atualização da conta do Administrator

    class Meta:
        db_table = 'client'  # Definindo o nome personalizado da tabela