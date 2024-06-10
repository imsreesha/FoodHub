# Generated by Django 5.0.3 on 2024-03-07 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliveryusermodel',
            old_name='Deliver_time',
            new_name='Delivery_time',
        ),
        migrations.AlterModelTable(
            name='addressmodel',
            table='Address_table',
        ),
        migrations.AlterModelTable(
            name='cartmodel',
            table='Cart_table',
        ),
        migrations.AlterModelTable(
            name='deliveryusermodel',
            table='Delivery_table',
        ),
        migrations.AlterModelTable(
            name='feedbackmodel',
            table='Feedback_table',
        ),
        migrations.AlterModelTable(
            name='ordermodel',
            table='Order_table',
        ),
        migrations.AlterModelTable(
            name='paymentmodel',
            table='Payment_table',
        ),
        migrations.AlterModelTable(
            name='reviewmodel',
            table='Review_table',
        ),
        migrations.AlterModelTable(
            name='userimagemodel',
            table='Userimage_table',
        ),
        migrations.AlterModelTable(
            name='usermodel',
            table='User_table',
        ),
    ]