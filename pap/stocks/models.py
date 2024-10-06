from django.db import models

# Modelos

class Produto(models.Model):
    nome = models.CharField(max_length=100)  # Nome do produto
    descricao = models.TextField(null=True, blank=True)  # Descrição do produto
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
    quantidade = models.IntegerField()  # Quantidade em stock
    data_criacao = models.DateTimeField(auto_now_add=True)  # Data de criação do produto
    data_atualizacao = models.DateTimeField(auto_now=True)  # Data de atualização do produto

    class Meta:
        db_table = 'produtos'  # Define o nome da tabela no banco de dados

    def __str__(self):
        return self.nome
