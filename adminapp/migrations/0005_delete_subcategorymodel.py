# Generated by Django 5.0.3 on 2024-03-25 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_remove_subcategorymodel_maincategory'),
        ('restaurantapp', '0003_itemmodel_image_itemmodel_rating_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subcategorymodel',
        ),
    ]
