from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import django

class Advocate(models.Model):
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, default="xxx")
    name = models.CharField(max_length=255, default="none")
    created_on = models.DateField(null=True)

    def __str__(self):
        return self.email + " " + self.name


class Shirt(models.Model):
    name = models.CharField(max_length=100)
    pic1_img_url = models.CharField(max_length=100)
    pic1_title = models.CharField(max_length=100, default="Front")
    pic2_img_url = models.CharField(max_length=100)
    pic2_title = models.CharField(max_length=100, default="Back")
    price = models.IntegerField(default=20)
    available = models.BooleanField(default=True)
    hex = models.CharField(max_length=10, default='#FFFFFF')

    def __str__(self):
        return self.name
    

class Order(models.Model):
    advocate = models.ForeignKey(Advocate, default=1, on_delete=models.CASCADE)
    shirt = models.ForeignKey(Shirt, default=1, on_delete=models.CASCADE)
    shirt_size = models.CharField(max_length=10)
    order_date = models.DateField(null=True)
    order_price = models.FloatField(default = 20)
    order_uuid = models.CharField(max_length=100)
    confirmed = models.FloatField(default = False)
    fulfilled = models.BooleanField(default = False)

    def __str__(self):
        return str(self.advocate) + " " + str(self.shirt) + " " + str(self.shirt_size)
    
    def confirm(self):
        self.confirmed = True
    
    def fulfill(self):
        self.fulfilled = True
