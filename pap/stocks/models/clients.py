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
    creation_date = models.DateTimeField(auto_now_add=True) # Data de criação
    update_date = models.DateTimeField(auto_now=True) # Data de atualização 

    class Meta:
        db_table = 'client'  # Definindo o nome personalizado da tabela

class ClientAddress(models.Model):
    # Chave Estrangeira
    client = models.ForeignKey(Client,on_delete=models.CASCADE,db_column='client_id')
    country = models.ForeignKey(Countries,on_delete=models.CASCADE,db_column='country_id') 
    # Atributos da tabela
    active = models.PositiveSmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1)  # Activo ou não
    address = models.CharField(max_length=200) # Morada 
    postalcode = models.CharField(max_length=20) # Código Postal
    locality = models.CharField(max_length=200) # Morada 
    city = models.CharField(max_length=200) # Cidade
    creation_date = models.DateTimeField(auto_now_add=True) # Data de criação 
    update_date = models.DateTimeField(auto_now=True) # Data de atualização 

    class Meta:
        db_table = 'client_address'  # Definindo o nome personalizado da tabela

class ClientLogs(models.Model):
    # Chave estrangeira
    client = models.OneToOneField(Client,on_delete=models.CASCADE,primary_key=True,db_column='client_id') 
    # Atributos da tabela
    datalog = models.DateTimeField(auto_now_add=True) # Data de criação 
    logfile = models.TextField(null=True, blank=True) # logfile

    class Meta:
        db_table = 'client_logs'  # Define o nome personalizado da tabela na base de dados