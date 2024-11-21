from django.db import models

class User(models.Model):
    # Atributos da tabela
    name = models.CharField(max_length=100) # Nome do utilizador
    email = models.EmailField(unique=True)  # Email do utilizador
    password = models.CharField(max_length=128)  # Hashed password
    position = models.CharField(max_length=50)  # Ex.: administrador, operador
    creation_date = models.DateTimeField(auto_now_add=True) # Data de criação do produto
    update_date = models.DateTimeField(auto_now=True) # Data de atualização do produto

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'