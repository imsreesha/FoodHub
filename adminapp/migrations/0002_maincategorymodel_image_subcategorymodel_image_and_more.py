# Generated by Django 5.0.3 on 2024-03-07 07:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maincategorymodel',
            name='Image',
            field=models.ImageField(null=True, upload_to='maincata/'),
        ),
        migrations.AddField(
            model_name='subcategorymodel',
            name='Image',
            field=models.ImageField(null=True, upload_to='subcata/'),
        ),
        migrations.AddField(
            model_name='subcategorymodel',
            name='Price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='subcategorymodel',
            name='Rating',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='subcategorymodel',
            name='Resturant_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
