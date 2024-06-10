from django.db import models

# Create your models here.
from restaurantapp.models import *
# Create your models here.
class Usermodel(models.Model):
    User_id=models.AutoField(primary_key=True)
    User_name=models.CharField(max_length=200)
    User_password=models.CharField(max_length=200)
    User_email=models.CharField(max_length=200)
    User_create_at=models.DateTimeField(auto_now_add=True)
    User_status=models.CharField(max_length=200,null=True)
    User_phone=models.CharField(max_length=100,null=True)
    class Meta:
        db_table='User_table'


    def __str__(self):
        return self.User_name

class Userimagemodel(models.Model):
    Image_id=models.IntegerField(primary_key=True)
    Image=models.ImageField()
    User_id=models.ForeignKey(Usermodel,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table='Userimage_table'

    def __str__(self):
        return self.User_id

class Addressmodel(models.Model):
    Address_id = models.AutoField(primary_key=True)  # Change the default value as needed

    User_id=models.ForeignKey(Usermodel,on_delete=models.CASCADE,null=True)
    Street=models.TextField()
    City = models.ForeignKey(Citymodel, on_delete=models.CASCADE,null=True)  # ForeignKey relationship with Citymodel
    State = models.ForeignKey(Statemodel, on_delete=models.CASCADE,null=True)  #
    Location=models.CharField(max_length=200)
    Pincode=models.CharField(max_length=100)
    class Meta:
        db_table='Address_table'

    def __str__(self):
        return self.User_id.User_name

class Cartmodel(models.Model):
    Cart_id = models.IntegerField(primary_key=True)
    User_id = models.ForeignKey(Usermodel, on_delete=models.CASCADE, null=True)
    Item_id = models.ForeignKey(Itemmodel,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table='Cart_table'

    def __str__(self):
        return self.Item_id


class Ordermodel(models.Model):
    Order_id = models.IntegerField(primary_key=True)
    User_id = models.ForeignKey(Usermodel, on_delete=models.CASCADE, null=True)
    Item = models.ForeignKey(Itemmodel,on_delete=models.CASCADE,null=True)
    Quantity=models.IntegerField()
    address=models.ForeignKey(Addressmodel,on_delete=models.CASCADE)
    Status = models.CharField(max_length=200)
    Order_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='Order_table'


class Feedbackmodel(models.Model):
    Item_id = models.ForeignKey(Itemmodel,on_delete=models.CASCADE,null=True)
    User_id = models.ForeignKey(Usermodel, on_delete=models.CASCADE, null=True)
    Feedback = models.TextField()
    Status = models.CharField(max_length=200)
    Rating = models.IntegerField()
    class Meta:
        db_table='Feedback_table'


class Deliveryusermodel(models.Model):
    Delivery_id = models.IntegerField(primary_key=True)
    Order_id = models.ForeignKey(Ordermodel, on_delete=models.CASCADE, null=True)
    Address = models.ForeignKey(Addressmodel,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=200)
    Delivery_time = models.DateTimeField()
    class Meta:
        db_table='Delivery_table'


class Paymentmodel(models.Model):
    payment_id=models.IntegerField(primary_key=True)
    User_id=models.ForeignKey(Usermodel,on_delete=models.CASCADE,null=True)
    Order_id=models.ForeignKey(Ordermodel,on_delete=models.CASCADE,null=True)
    Amount=models.FloatField()
    Paymentmethod=models.CharField(max_length=200)
    Time=models.DateTimeField()
    class Meta:
        db_table='Payment_table'

class Reviewmodel(models.Model):
    Review_id = models.IntegerField(primary_key=True)
    User_id = models.ForeignKey(Usermodel, on_delete=models.CASCADE, null=True)
    Item = models.ForeignKey(Itemmodel, on_delete=models.CASCADE, null=True)
    Comments = models.TextField()
    rating = models.IntegerField()
    class Meta:
        db_table='Review_table'
class Wishlistmodel(models.Model):
    Wishlist_id = models.AutoField(primary_key=True)
    User = models.ForeignKey(Usermodel,on_delete=models.CASCADE,null=True)
    Item =models.ForeignKey(Itemmodel,on_delete=models.CASCADE,null=True)


    class Meta:
        db_table = 'Wishlist'

    def __str__(self):
        return self.Item.Item_name






