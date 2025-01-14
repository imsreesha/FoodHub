# Generated by Django 5.0.3 on 2024-05-07 07:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0006_alter_itemmodel_item_id'),
        ('userapp', '0004_wishlistmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressmodel',
            name='City',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurantapp.citymodel'),
        ),
        migrations.AddField(
            model_name='addressmodel',
            name='State',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurantapp.statemodel'),
        ),
    ]
