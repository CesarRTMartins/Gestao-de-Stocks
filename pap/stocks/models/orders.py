from django.db import models
from .clients import *
from .payments_bills import *
from .products import *
from .suppliers import * 

class OrderClient(models.Model):
    # Chave estrangeira
    client = models.ForeignKey(Client,on_delete=models.CASCADE,db_column='client_id')
    # Atributos da tabela
    orderdate = models.DateTimeField(auto_now_add=True) # Data de criação da order
    closed = models.PositiveSmallIntegerField(choices=[(0, 'Closed'), (1, 'Active')], default=1)  # Fechado ou não
    totalvalue = models.DecimalField(max_digits=10, decimal_places=2)  # Valor Total
    
    class Meta:
        db_table = 'order_client'  # Define o nome personalizado da tabela na base de dados

class OrderClientBill(models.Model):
    # Chave estrangeira
    order = models.ForeignKey(OrderClient,on_delete=models.CASCADE,primary_key=True,db_column='order_client_id')
    # Atributos da tabela
    clientname = models.CharField(max_length=200) # Nome do Cliente 
    clientnif = models.CharField(max_length=12) # Nome do Cliente 
    clientadress = models.CharField(max_length=200) # Nome do Cliente 
    clientpostalcode = models.CharField(max_length=20) # Nome do Cliente 
    clientlocality = models.CharField(max_length=200) # Nome do Cliente 
    clientcity = models.CharField(max_length=200) # Nome do Cliente 

    class Meta:
        db_table = 'order_client_bill'  # Define o nome personalizado da tabela na base de dados

class OrderClientPayment(models.Model):
    # Chaves estrangeiras
    order = models.ForeignKey(OrderClient,on_delete=models.CASCADE,primary_key=True,db_column='order_id')
    paymenttype = models.ForeignKey(PaymentType,on_delete=models.CASCADE,db_column='payment_type_id')
    # Atributos da tabela
    paymentvalue = models.DecimalField(max_digits=10, decimal_places=2)  # Valor Total
    totalvalue = models.TextField(max_length=200)  # Valor Total

    class Meta:
        db_table = 'order_client_payment'  # Define o nome personalizado da tabela na base de dados
    
class OrderClientProduct(models.Model):
    # Chaves estrangeira
    order = models.ForeignKey(OrderClient,on_delete=models.CASCADE,primary_key=True,db_column='order_id')  
    product = models.ForeignKey(Products,on_delete=models.CASCADE,db_column='product_id')
    # Chave estrangeira
    productvalue = models.DecimalField(max_digits=10, decimal_places=2)  # Valor Total
    productref = models.CharField(max_length=50) # Referência do produto
    productsize = models.CharField(max_length=50) # Tamanho do Produto
    quantity = models.IntegerField() # Quantidade do Produto
    weight = models.DecimalField(max_digits=10, decimal_places=5)  # Valor Total

    class Meta:
        db_table = 'order_client_product' # Nome da tabela na base de dados

class OrderSupplier(models.Model):
    # Chaves estrangeira
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,db_column='supplier_id')
    # Atributos da tabela
    orderdate = models.DateTimeField(auto_now_add=True) # Data de criação da order 
    closed = models.PositiveSmallIntegerField(choices=[(0, 'Closed'), (1, 'Active')], default=1)  # Fechado ou não
    totalvalue = models.DecimalField(max_digits=10, decimal_places=2)  # Valor Total

    class Meta:
        db_table = 'order_supplier' # Nome da tabela na base de dados

class OrderSupplierProduct(models.Model):
    # Chaves estrangeira
    order = models.ForeignKey(OrderClient,on_delete=models.CASCADE,primary_key=True,db_column='order_id')  
    product = models.ForeignKey(Products,on_delete=models.CASCADE,db_column='product_id')
    # Chave estrangeira
    productvalue = models.DecimalField(max_digits=10, decimal_places=2)  # Valor Total
    productref = models.CharField(max_length=50) # Referência do produto
    productsize = models.CharField(max_length=50) # Tamanho do Produto
    quantity = models.IntegerField() # Quantidade do Produto
    weight = models.DecimalField(max_digits=10, decimal_places=5)  # Valor Total

    class Meta:
        db_table = 'order_supplier_product' # Nome da tabela na base de dados