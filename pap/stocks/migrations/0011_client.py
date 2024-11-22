# Generated by Django 5.1.1 on 2024-11-22 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0010_alter_clienttype_category_alter_products_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveSmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1)),
                ('nif', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('clienttype', models.ForeignKey(db_column='client_type_id', on_delete=django.db.models.deletion.CASCADE, to='stocks.clienttype')),
                ('country', models.ForeignKey(db_column='country_id', on_delete=django.db.models.deletion.CASCADE, to='stocks.countries')),
            ],
        ),
    ]
