from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import BuyerSerializer, ShirtSerializer, OrderSerializer
from .models import Buyer, Shirt, Order

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
    
