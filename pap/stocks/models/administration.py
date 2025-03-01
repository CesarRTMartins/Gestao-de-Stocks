from django.db import models
from .common import Modules

class Administrator(models.Model):
    # Atributos da tabela
    name = models.CharField(max_length=50)  # Nome do Administrator
    email = models.EmailField(unique=True)  # Email do Administrator
    password = models.CharField(max_length=128)  # Password do Administrator
    creation_date = models.DateTimeField(auto_now_add=True) # Data de criação da conta do Administrator
    update_date = models.DateTimeField(auto_now=True) # Data de atualização da conta do Administrator
    active = models.PositiveSmallIntegerField(
        choices=[(0, 'Inactive'), 
                (1, 'Active')], 
                default=1 # Activo ou não)
        )

    class Meta:
        db_table = 'administrator'  # Define o nome personalizado da tabela na base de dados

    def __str__(self):  
        return self.name
    
class AdministratorLogs(models.Model):
    # Chave estrangeira para o modelo Administrator
    administrator = models.OneToOneField(Administrator,on_delete=models.CASCADE,primary_key=True,db_column='administrator_id') 
    # Atributos da tabela
    datalog = models.DateTimeField(auto_now_add=True) # Data de criação da conta do Administrator
    logfile = models.TextField(null=True, blank=True) # logfile

    class Meta:
        db_table = 'administrator_logs'  # Define o nome personalizado da tabela na base de dados

class AdministratorModules(models.Model):
    # Chave estrangeira para o id do modelo Administrator
    administrator = models.ForeignKey(Administrator,on_delete=models.CASCADE,primary_key=True,db_column='administrator_id')
    # Chave estrangeira para o modelo Modules
    module = models.ForeignKey(Modules, on_delete=models.CASCADE)
    # Atributos da tabela
    pView = models.PositiveSmallIntegerField(null=True,)
    pInsert = models.PositiveSmallIntegerField(null=True,)
    pUpdate = models.PositiveSmallIntegerField(null=True,)
    pDelete = models.PositiveSmallIntegerField(null=True,)
    creation_date = models.DateTimeField(auto_now_add=True) # Data de criação 
    update_date = models.DateTimeField(auto_now=True) # Data de atualização

    class Meta:
        db_table = 'administrator_modules'  # Define o nome personalizado da tabela na base de dados