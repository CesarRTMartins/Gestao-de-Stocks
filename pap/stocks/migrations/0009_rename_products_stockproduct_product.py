# Generated by Django 5.1.1 on 2024-11-18 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0008_countries'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockproduct',
            old_name='products',
            new_name='product',
        ),
    ]
