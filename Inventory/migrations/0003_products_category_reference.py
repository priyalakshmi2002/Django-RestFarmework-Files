# Generated by Django 5.1.2 on 2024-10-17 07:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category_reference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Inventory.category'),
        ),
    ]
