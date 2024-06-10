from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator


from adminapp.models import *
# Create your models here.
class Statemodel(models.Model):
    state_id=models.IntegerField(primary_key=True)
    state_name=models.CharField(max_length=100)
    class Meta:
        db_table='State_table'

    def __str__(self):
        return self.state_name

class Citymodel(models.Model):
    city_id=models.IntegerField(primary_key=True)
    city_name=models.CharField(max_length=100)
    state=models.ForeignKey(Statemodel,on_delete=models.CASCADE)
    class Meta:
        db_table='City_table'

    def __str__(self):
        return self.city_name

class Restaurantmodel(models.Model):
    Restaurant_id=models.IntegerField(primary_key=True)
    Restaurant_name=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
    License=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    City=models.ForeignKey(Citymodel,on_delete=models.CASCADE)
    Discription=models.TextField()
    Phone_no=models.CharField(max_length=100)
    Email=models.CharField(max_length=200)
    Image=models.ImageField()
    host_status=models.CharField(max_length=100)
    class Meta:
        db_table='Restaurant_table'

    def __str__(self):
        return self.Restaurant_name

class Itemmodel(models.Model):
    Item_id=models.AutoField(primary_key=True)
    Item_name=models.CharField(max_length=200)
    Description=models.TextField()
    Price=models.FloatField()
    Quantity=models.CharField(max_length=200)
    Start_time=models.DateTimeField()
    End_time=models.DateTimeField()
    Image=models.ImageField(upload_to='subcat/',null=True)
    Category=models.ForeignKey(Maincategorymodel,on_delete=models.CASCADE,null=True)
    host_id=models.ForeignKey(Restaurantmodel,on_delete=models.CASCADE)
    status=models.CharField(max_length=100)
    is_in_wishlist=models.BooleanField(default=False,null=True)
    Rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True)
    class Meta:
        db_table='Item_table'

    def __str__(self):
        return self.Item_name
class Eventmodel(models.Model):
    Event_id=models.IntegerField(primary_key=True)
    Event=models.CharField(max_length=250)
    Description=models.TextField()
    start_date=models.DateField()
    End_date=models.DateField()
    status=models.CharField(max_length=100)
    class Meta:
        db_table='Event_table'

    def __str__(self):
        return self.Event

class Discountmodel(models.Model):
    Discount_id=models.IntegerField(primary_key=True)
    Item_id=models.ForeignKey(Itemmodel,on_delete=models.CASCADE,null=True)
    Discount=models.CharField(max_length=200)
    Event=models.ForeignKey(Eventmodel,on_delete=models.CASCADE)
    class Meta:
        db_table='Discount_table'

    def __str__(self):
        return self.Event

class Couponmodel(models.Model):
    Coupon_id=models.AutoField(primary_key=True)
    Coupon_code=models.CharField(max_length=10)
    is_expired=models.BooleanField(default=False)
    discount_price=models.IntegerField(null=True)
    minimum_amnt=models.IntegerField()

    class Meta:
        db_table='Coupon'

    def __str__(self):
        return self.Coupon_code