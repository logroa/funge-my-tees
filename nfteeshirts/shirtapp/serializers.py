from rest_framework import serializers
from .models import Buyer, Shirt, Order
from datetime import datetime

class BuyerSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)
    created_on = serializers.DateTimeField(default=datetime.now())
    last_order = serializers.DateTimeField(default=datetime.now())

    class Meta:
        model = Buyer
        fields = ('__all__')


class ShirtSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    front_img_url = serializers.CharField(max_length=100)
    back_img_url = serializers.CharField(max_length=100)
    price = serializers.IntegerField(default=20)
    available = serializers.BooleanField(default=True)
    hex = serializers.CharField(max_length=10)

    class Meta:
        model = Shirt
        fields = ('__all__')


class OrderSerializer(serializers.ModelSerializer):
    buyer_id = serializers.PrimaryKeyRelatedField(queryset=Buyer.objects.all())
    shirt_id = serializers.PrimaryKeyRelatedField(queryset=Shirt.objects.all())
    shirt_size = serializers.CharField(max_length=10, required=False, default='L')
    order_date = serializers.DateTimeField(default=datetime.now())
    order_num = serializers.IntegerField(default=1)

    class Meta:
        model = Order
        fields = ('__all__')