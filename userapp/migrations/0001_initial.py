# Generated by Django 5.0.3 on 2024-03-06 07:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurantapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addressmodel',
            fields=[
                ('Address_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Street', models.TextField()),
                ('Location', models.CharField(max_length=200)),
                ('Pincode', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usermodel',
            fields=[
                ('User_id', models.IntegerField(primary_key=True, serialize=False)),
                ('User_name', models.CharField(max_length=200)),
                ('User_password', models.CharField(max_length=200)),
                ('User_email', models.CharField(max_length=200)),
                ('User_create_at', models.DateTimeField(auto_now_add=True)),
                ('User_status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ordermodel',
            fields=[
                ('Order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Quantity', models.IntegerField()),
                ('Status', models.CharField(max_length=200)),
                ('Order_time', models.DateTimeField(auto_now_add=True)),
                ('Item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurantapp.itemmodel')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.addressmodel')),
                ('User_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.usermodel')),
            ],
        ),
        migrations.CreateModel(
            name='Deliveryusermodel',
            fields=[
                ('Delivery_id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=200)),
                ('Deliver_time', models.DateTimeField()),
                ('Address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.addressmodel')),
                ('Order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.ordermodel')),
            ],
        ),
        migrations.CreateModel(
            name='Userimagemodel',
            fields=[
                ('Image_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Image', models.ImageField(upload_to='')),
                ('User_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.usermodel')),
            ],
        ),
        migrations.CreateModel(
            name='Reviewmodel',
            fields=[
                ('Review_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Comments', models.TextField()),
                ('rating', models.IntegerField()),
                ('Item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurantapp.itemmodel')),
                ('User_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.usermodel')),
            ],
        ),
        migrations.CreateModel(
            name='Paymentmodel',
            fields=[
                ('payment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Amount', models.FloatField()),
                ('Paymentmethod', models.CharField(max_length=200)),
                ('Time', models.DateTimeField()),
                ('Order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.ordermodel')),
                ('User_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.usermodel')),
            ],
        ),
        migrations.CreateModel(
            name='Feedbackmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feedback', models.TextField()),
                ('Status', models.CharField(max_length=200)),
                ('Rating', models.IntegerField()),
                ('Item_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurantapp.itemmodel')),
                ('User_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.usermodel')),
            ],
        ),
        migrations.CreateModel(
            name='Cartmodel',
            fields=[
                ('Cart_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Item_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurantapp.itemmodel')),
                ('User_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.usermodel')),
            ],
        ),
        migrations.AddField(
            model_name='addressmodel',
            name='User_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.usermodel'),
        ),
    ]
