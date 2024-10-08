from django.db import models

# Modelos

class Products(models.Model):
        name = models.CharField(max_length=100)  # Nome do produto
        description = models.TextField(null=True, blank=True)  # Descrição do produto
        price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
        quantity = models.IntegerField()  # Quantidade em stock
        creation_date = models.DateTimeField(auto_now_add=True)  # Data de criação do produto
        update_date = models.DateTimeField(auto_now=True)  # Data de atualização do produto

        class Meta:
            db_table = 'products'  # Define o nome da tabela no banco de dados

        def __str__(self):
            return self.name

