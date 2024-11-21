from django.db import models

class Size(models.Model):
    # Atributos da tabela
    active = models.PositiveSmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1)  # Activo ou não
    size = models.CharField(max_length=50) # Tamanho 
    class Meta:
        db_table = 'size'

class ProductCategory(models.Model):
    # Atributos da tabela
    name = models.CharField(max_length=200) # Nome da Categoria
    creation_date = models.DateTimeField(auto_now_add=True) # Data de criação da categoria
    update_date = models.DateTimeField(auto_now=True) # Data de atualização da categoria

    class Meta:
        db_table = 'product_category'  # Definindo o nome personalizado da tabela
        
class Products(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,null=True,db_column='product_category_id')
    # Atributos da tabela
    name = models.CharField(max_length=100)  # Nome do produto
    description = models.TextField(null=True, blank=True)  # Descrição do produto
    reference = models.CharField(max_length=50,null=True,blank=True) # Referência do Produto
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
    weight = models.DecimalField(max_digits=10, decimal_places=5,null=True)  # Preço do produto
    img = models.TextField(null=True,blank=True)
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

class ProductSize(models.Model):
    # Chave estrageira do modelo Products
    product = models.OneToOneField(
        Products,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column='product_id'  # Define o nome da coluna no banco de dados
        )
    # Chave estrageira do modelo Size
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    # Atributos da tabela
    creation_date = models.DateTimeField(auto_now_add=True) # Data de criação do produto
    update_date = models.DateTimeField(auto_now=True) # Data de atualização do produto

    class Meta:
        db_table = 'product_size'  # Definindo o nome personalizado da tabela
    
    def __str__(self):  
        return f"Size: {self.size} - Product id: {self.product.id}"

class StockProduct(models.Model):
    # Chave estrangeira do modelo Products
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='stocks') # Products id
    # Atributos da tabela
    quantity = models.IntegerField()  # Quantidade em stock
    entry_date = models.DateTimeField(auto_now_add=True)  # Data de entrada em stock
    update_date = models.DateTimeField(auto_now=True)  # Data da última atualização do stock

    class Meta:
        db_table = 'product_stock'  # Definindo o nome personalizado da tabela

    def __str__(self):
        return f"Stock for {self.product.name} - Quantity: {self.quantity}" 

