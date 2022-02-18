from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import AdvocateSerializer, ShirtSerializer, OrderSerializer
from .models import Advocate, Shirt, Order

from datetime import date

class AdvocateViews(APIView):
    """
    API endpoint returning buyers.
    """
    def get(self, request, id=None):
        if id:
            adv = Advocate.objects.get(id=id)
            serializer = AdvocateSerializer(adv)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        shirts = Advocate.objects.all()
        serializer = ShirtSerializer(shirts, many=True)
        return Response({"status": "success", "Access-Control-Allow-Origin": "*", "data": serializer.data}, status=status.HTTP_200_OK)   

class ShirtViews(APIView):
    """
    API endpoint returning available shirts.
    """
    def post(self, request):
        serializer = ShirtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id=None):
        if id:
            shirt = Shirt.objects.get(id=id)
            serializer = ShirtSerializer(shirt)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        shirts = Shirt.objects.filter(available=True)
        serializer = ShirtSerializer(shirts, many=True)
        return Response({"status": "success", "Access-Control-Allow-Origin": "*", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def patch(self, request, id=None):
        shirt = Shirt.objects.get(id=id)
        serializer = ShirtSerializer(shirt, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
    
    def delete(self, request, id=None):
        shirt = get_object_or_404(Shirt, id=id)
        shirt.delete()
        return Response({"status": "success", "data": "Item Deleted"})

class OrderViews(APIView):
    """
    API endpoint for placing orders.
    """
    def post(self, request):
        data = {
            'email': request.data.get('email'),
            'name': request.data.get('name'),
            'phone_number': request.data.get('phone_number'),
            'id': request.data.get('id'),
            'order_price': request.data.get('order_price'),
            'orders': list(request.data.get('orders').values())
        }
        try:
            buyer = Advocate.objects.get(email = data['email'])
            buyer.name = data['name']
            buyer.phone_number = data['phone_number']
            buyer.save()
        except:
            buyer = Advocate(email=data['email'], name=data['name'],
                          phone_number=data['phone_number'], created_on=date.today())
            buyer.save()
        orders = []
        for o in data['orders']:
            data1 = {
                'advocate': buyer.id,
                'shirt': data['id'],
                'shirt_size': o,
                'order_date': date.today(),
                'order_price': data['order_price'],
                'fulfilled': False
            }
            orders.append(data1)
        serializer = OrderSerializer(data=orders, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    
