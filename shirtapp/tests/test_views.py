import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from shirtapp.views import OrderViews
from ..models import Advocate, Shirt, Order
from ..serializers import AdvocateSerializer, ShirtSerializer, OrderSerializer

client = Client()

class CreateOrderTest(TestCase):
    """Testing that order works"""

    def setUp(self):
        self.valid_order = {
            'email': 'ltroach85@gmail.com',
            'name': 'Logan Test',
            'phone_number': '9188845288',
            'id': 1,
            'order_price': 20,
            'orders': {
                'size0': 'L'
            }
        }

        self.shirt = {
            "name": "TEST SHIRT",
            "pic1_img_url": "TESTpic1",
            "pic1_title": "front",
            "pic2_img_url": "TESTpic2",
            "pic2_title": "back",
            "price": 20,
            "available": True,
            "hex": "#FFFFFF"
        }

        self.invalid_order = {
            'email': 'bademail'
        }

    def test_create_valid_shirt_then_order(self):
        response = client.post(
            reverse('shirt-guy'),
            data=json.dumps(self.shirt),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)\

        self.valid_order['id'] = response.data["data"]["id"]

        response = client.post(
            reverse('order-shirt'),
            data=json.dumps(self.valid_order),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
