from rest_framework import serializers
from .models import Advocate, Shirt, Order, Hit
from datetime import date


class AdvocateSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=15)
    name = serializers.CharField(max_length=255)
    created_on = serializers.DateTimeField(default=date.today())

    class Meta:
        model = Advocate
        fields = ('__all__')


class ShirtSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    pic1_img_url = serializers.CharField(max_length=100)
    pic1_title = serializers.CharField(max_length=100)
    pic2_img_url = serializers.CharField(max_length=100)
    pic2_title = serializers.CharField(max_length=100)
    price = serializers.IntegerField(default=20)
    available = serializers.BooleanField(default=True)
    hex = serializers.CharField(max_length=10)

    class Meta:
        model = Shirt
        fields = ('__all__')


class OrderSerializer(serializers.ModelSerializer):
    advocate = serializers.PrimaryKeyRelatedField(queryset=Advocate.objects.all())
    shirt = serializers.PrimaryKeyRelatedField(queryset=Shirt.objects.all())
    shirt_size = serializers.CharField(max_length=10, required=False, default='L')
    order_date = serializers.DateField(default=date.today())
    order_price = serializers.FloatField(default = 20)
    order_uuid = serializers.CharField(max_length=100)
    confirmed = serializers.BooleanField(default=False)
    fulfilled = serializers.BooleanField(default=False)

    class Meta:
        model = Order
        fields = ('__all__')

class HitSerializer(serializers.ModelSerializer):
    ip_address = serializers.CharField(max_length=30)
    when = serializers.CharField()

    class Meta:
        model = Hit
        fields = ('__all__')