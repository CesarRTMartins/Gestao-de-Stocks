from django.db import models

class Modules(models.Model):
    # Atributos da tabela
    idModule = models.IntegerField()  # Id do Module
    codModule = models.CharField(max_length=50)  # Codigo do Module
    module = models.CharField(max_length=250)  # Modulo

    class Meta:
        db_table = 'modules'  # Define o nome personalizado da tabela na base de dados

    def __str__(self):
        return f"{self.codModule} - {self.module}"

class Countries(models.Model):
    # Atributos da tabela
    country = models.CharField(max_length=200)  # País
    cod = models.CharField(max_length=2)  # Cod do País
    indicative = models.CharField(max_length=10)  # Indicativo do País
    active = models.PositiveSmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1)  # Activo ou não

    class Meta:
        db_table = 'countries'  # Define o nome personalizado da tabela na base de dados

    def __str__(self):
        return f"{self.country} ({self.cod})"   
