# Generated by Django 5.1.1 on 2024-11-22 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0008_alter_clienttype_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(db_column='product_category_id', on_delete=django.db.models.deletion.CASCADE, to='stocks.productcategory'),
        ),
    ]