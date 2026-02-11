from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.
# pet model


# shop signup page (Registration)
class Shop_signup_table(models.Model):
    shop_name=models.CharField(max_length=100)
    owner_name=models.CharField(max_length=100)
    shop_photo=models.FileField()
    email=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=10)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=10)
    district=models.CharField(max_length=50)
    pin=models.CharField(max_length=10)
    LOGIN=models.ForeignKey(User,on_delete=models.CASCADE)


# pet model
class pet(models.Model):
    name=models.CharField(max_length=100)
    breed=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    age=models.IntegerField()
    vaccinated=models.CharField(max_length=10) # yes/no option only.
    description=models.TextField(blank=True, null=True)
    photo=models.FileField()
    shop=models.ForeignKey(Shop_signup_table, on_delete=models.CASCADE)

# User signup page (Registration)
class User_signup_table(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255, blank=True)
    profile_photo = models.FileField()
    
    LOGIN = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

# product table
class Product_table(models.Model):
    Product_Name=models.CharField(max_length=100)
    Details=models.CharField(max_length=300)
    Photo=models.FileField()
    Price=models.IntegerField()
    Quantity=models.IntegerField()
    type=models.CharField(max_length=50)
    SHOP=models.ForeignKey(Shop_signup_table,on_delete=models.CASCADE)

#  product cart 
class Cart_table(models.Model):
    PRODUCT=models.ForeignKey(Product_table,on_delete=models.CASCADE)
    date=models.DateField()
    Quantity=models.IntegerField()
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    Total_amount=models.BigIntegerField()

    

# order_table (main)
class Order_table_main(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    Date=models.DateField()
    Status=models.CharField(max_length=20,default="pending")
    Amount=models.IntegerField()


# order_table (sub)
class Order_table_sub(models.Model):
    PRODUCT=models.ForeignKey(Product_table,on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    Total_amount=models.BigIntegerField(default=0)
    Status=models.CharField(max_length=20,default="pending")
    ORDER=models.ForeignKey(Order_table_main,on_delete=models.CASCADE)  # order_table_main

# user complaint table
class User_complaint_table(models.Model):
    Date=models.DateField()
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    Complaint=models.TextField()
    Reply=models.TextField(default="no reply")
    


class PasswordResetOTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return (timezone.now() - self.created_at).seconds > 300   # 5 minutes



    
