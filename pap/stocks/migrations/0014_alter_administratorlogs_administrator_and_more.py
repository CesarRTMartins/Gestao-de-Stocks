# Generated by Django 5.1.1 on 2024-11-18 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0013_administratormodules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administratorlogs',
            name='administrator',
            field=models.OneToOneField(db_column='administrator_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='stocks.administrator'),
        ),
        migrations.AlterField(
            model_name='administratormodules',
            name='administrator',
            field=models.OneToOneField(db_column='administrator_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='stocks.administrator'),
        ),
    ]