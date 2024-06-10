from django.db import models


class Adminmodel(models.Model):
    Admin_id=models.AutoField(primary_key=True)
    Username=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Phonenumber=models.CharField(max_length=100)
    class Meta:
        db_table='Admin_table'

    def __str__(self):
        return self.Username


class Maincategorymodel(models.Model):
    Maincategory_id=models.IntegerField(primary_key=True)
    Maincategory=models.CharField(max_length=200)
    Image=models.ImageField(upload_to='maincata/',null=True)

    class Meta:
        db_table='Maincategory_table'

    def __str__(self):
        return self.Maincategory



