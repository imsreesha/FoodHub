# Generated by Django 5.0.3 on 2024-03-07 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='citymodel',
            table='City_table',
        ),
        migrations.AlterModelTable(
            name='discountmodel',
            table='Discount_table',
        ),
        migrations.AlterModelTable(
            name='eventmodel',
            table='Event_table',
        ),
        migrations.AlterModelTable(
            name='itemmodel',
            table='Item_table',
        ),
        migrations.AlterModelTable(
            name='restaurantmodel',
            table='Restaurant_table',
        ),
        migrations.AlterModelTable(
            name='statemodel',
            table='State_table',
        ),
    ]
