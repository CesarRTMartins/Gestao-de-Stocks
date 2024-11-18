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

    def save(self, *args, **kwargs):
        # Guarda o produto
        super(Products, self).save(*args, **kwargs)

        # Cria automaticamente um registro na tabela StockProduct
        StockProduct.objects.create(product=self, quantity=self.quantity)

    def __str__(self):
        return self.name

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

class StockProduct(models.Model):
    # Chave estrangeira para o modelo Products
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='stocks') # Products id
    
    # Atributos da tabela
    quantity = models.IntegerField()  # Quantidade em stock
    entry_date = models.DateTimeField(auto_now_add=True)  # Data de entrada em stock
    update_date = models.DateTimeField(auto_now=True)  # Data da última atualização do stock

    class Meta:
        db_table = 'stock_product'  # Definindo o nome personalizado da tabela

    def __str__(self):
        return f"Stock for {self.product.name} - Quantity: {self.quantity}" 

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
