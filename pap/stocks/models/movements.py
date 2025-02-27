from django.db import models
from .products import *


class Movements(models.Model):


    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="movements")
    stock = models.ForeignKey(StockProduct, on_delete=models.CASCADE, related_name="movements", null=True, blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Opcional para saídas
    movement_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'movements'