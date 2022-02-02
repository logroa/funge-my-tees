from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import BuyerSerializer, ShirtSerializer, OrderSerializer
from .models import Buyer, Shirt, Order

from datetime import datetime

class ShirtViews(APIView):
    """
    API endpoint returning available shirts.
    """
    def post(self, request):
        serializer = ShirtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
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
        try:
            buyer = Buyer.objects.get(email = request['email'])
            buyer.name = request['name']
            buyer.phone_number = request['phone_number']
            buyer.save()
        except:
            buyer = Buyer(email=request['email'], name=request['name'],
                          phone_number=request['phone_number'], created_on=datetime.now())
            buyer.save()
        orders = []
        for o in request['orders']:
            data = {
                'buyer_id': buyer,
                'shirt_id': Shirt.objects.get(id=request['id']),
                'shirt_size': o['shirt_size'],
                'order_date': datetime.now(),
                'order_price': o['order_price'],
                'fulfilled': False
            }
            orders.append(data)
        serializer = OrderSerializer(data=orders)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    
