# Generated by Django 5.1.1 on 2024-11-22 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0007_alter_clienttype_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clienttype',
            name='category',
            field=models.ForeignKey(db_column='client_category_id', on_delete=django.db.models.deletion.CASCADE, to='stocks.clientcategory'),
        ),
    ]