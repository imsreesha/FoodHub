# Generated by Django 5.0.3 on 2024-03-25 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_subcategorymodel_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategorymodel',
            name='Maincategory',
        ),
    ]
