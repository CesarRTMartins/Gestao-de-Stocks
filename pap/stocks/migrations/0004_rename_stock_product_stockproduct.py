# Generated by Django 5.1.1 on 2024-10-19 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_alter_stock_product_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='stock_Product',
            new_name='StockProduct',
        ),
    ]
