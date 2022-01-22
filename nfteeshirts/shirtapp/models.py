from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Buyer(models.Model):
    email = models.CharField(max_length=255)
    created_on = models.DateTimeField(default=datetime.now())
    last_order = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.email


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
    buyer_id = models.ForeignKey(Buyer, default=1, on_delete=models.CASCADE)
    shirt_id = models.ForeignKey(Shirt, default=1, on_delete=models.CASCADE)
    shirt_size = models.CharField(max_length=10)
    order_date = models.DateTimeField(default=datetime.now())
    order_num = models.IntegerField(default=1)

    def __str__(self):
        return str(self.buyer_id) + " " + str(self.shirt_id) + " " + str(self.shirt_size)
