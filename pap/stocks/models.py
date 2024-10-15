from django.db import models

# Modelos

class Products(models.Model):
        # Atributos da tabela
        name = models.CharField(max_length=100)  # Nome do produto
        description = models.TextField(null=True, blank=True)  # Descrição do produto
        price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
        quantity = models.IntegerField()  # Quantidade em stock
        creation_date = models.DateTimeField(auto_now_add=True)  # Data de criação do produto
        update_date = models.DateTimeField(auto_now=True)  # Data de atualiza  ção do produto

        class Meta:
            db_table = 'products'  # Define o nome da tabela no banco de dados
            verbose_name = 'Product'  # Nome singular
            verbose_name_plural = 'Products'  # Nome plural correto

        def __str__(self):
            return self.name

class User(models.Model):
    # Atributos da tabela
    name = models.CharField(max_length=100) # Nome do utilizador
    email = models.EmailField(unique=True)  # Email do utilizador
    password = models.CharField(max_length=128)  # Hashed password
    position = models.CharField(max_length=50)  # Ex.: administrador, operador
    creation_date = models.DateTimeField(auto_now_add=True) # Data de criação do produto
    update_date = models.DateTimeField(auto_now=True) # Data de atualiza  ção do produto

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'