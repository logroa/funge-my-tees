import os
from django.shortcuts import render
from django.http import HttpResponse
import json
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator
from django.db.models import Count
from django.shortcuts import render, redirect
from django.db.models.functions import TruncDate
from pytz import timezone
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import AdvocateSerializer, ShirtSerializer, OrderSerializer, HitSerializer
from .models import Advocate, Shirt, Order, Hit
from .messager import Texter

from datetime import datetime
from datetime import date
from dotenv import load_dotenv

load_dotenv()


class AdvocateViews(APIView):
    """
    API endpoint returning buyers.
    """
    @method_decorator(login_required)
    def get(self, request, id=None):
        if id:
            adv = Advocate.objects.get(id=id)
            serializer = AdvocateSerializer(adv)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        advos = Advocate.objects.all()
        serializer = AdvocateSerializer(advos, many=True)
        return Response({"status": "success", "Access-Control-Allow-Origin": "*", "data": serializer.data}, status=status.HTTP_200_OK)   


def add_hit(ip_address):
    """
    Adds IP Address of someone who viewed website to database
    """
    try:
        hit = Hit(ip_address=ip_address, when=datetime.now(timezone('America/Chicago')))
        hit.save()
    except Exception as e:
        print("Error: ", e)
        print("Missed this IP: ", ip_address)
    # probably some text functionality if a lot of traffic in one sitting right?


def traffic_stats(request, template_name="traffic_stats.html"):
    """
    View stats of traffic
    """
    hits = Hit.objects.annotate(hit_date=TruncDate('when'))\
        .values('hit_date')\
        .annotate(hit_count=Count('ip_address'))
    return render(request, template_name, {"hits": hits})

class ShirtViews(APIView):
    """
    API endpoint returning available shirts.
    """
    @method_decorator(login_required)
    def post(self, request):
        serializer = ShirtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id=None):
        add_hit(request.META.get('REMOTE_ADDR'))
        if id:
            shirt = Shirt.objects.get(id=id)
            serializer = ShirtSerializer(shirt)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        shirts = Shirt.objects.filter(available=True)
        serializer = ShirtSerializer(shirts, many=True)
        return Response({"status": "success", "Access-Control-Allow-Origin": "*", "data": serializer.data}, status=status.HTTP_200_OK)
    
    @method_decorator(login_required)
    def patch(self, request, id=None):
        shirt = Shirt.objects.get(id=id)
        serializer = ShirtSerializer(shirt, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
    
    @method_decorator(login_required)
    def delete(self, request, id=None):
        shirt = get_object_or_404(Shirt, id=id)
        shirt.delete()
        return Response({"status": "success", "data": "Item Deleted"})


class OrderViews(APIView):
    """
    API endpoint for placing orders.
    """
    def post(self, request):
        print("request data: ", request.data)
        print("request: ", request)

        data = {
            'email': request.data.get('email'),
            'name': request.data.get('name'),
            'phone_number': request.data.get('phone_number'),
            'id': request.data.get('id'),
            'order_price': request.data.get('order_price'),
            'orders': list(request.data.get('orders').values())
        }

        texter = Texter()
        order_uuid = str(uuid.uuid4())
        ordered_shirt = Shirt.objects.get(id=data["id"])
        message = f"""
            Holy shit, {data['name'].split()[0]}! I can't believe you actually bought this thing.  That's 
            hilarious.  Obviously you didn't pay directly through the site, and the reason for that
            is, well, we at FungeMyTees are just not that good at coding.  Credit card numbers? Actual money?? Security???
            We're well aware of our limitations.  
            """
            
        message_pt2 = f"""So here's what we're going to do.  If you do actually want the 
            shirt, which does reflect poorly on you, click the link at the bottom of this text and we'll venmo request 
            you based on this phone number for your order ({len(data['orders'])} '{ordered_shirt.name}' for ${len(data['orders'])*data['order_price']}).  
            If venmo doesn't work for you but you still want a shirt, email fungemytees@gmail.com and let us
            know what's up.
        """
        link = f"\n\n{os.environ.get('API_URL', 'envwrong')}/api/confirmation/{order_uuid}"
        
        text_body = " ".join(message.split()) + "\n\n" + " ".join(message_pt2.split()) + link

        new_user = False
        try:
            adv = Advocate.objects.get(email = data['email'])
            adv.name = data['name']
        except:
            adv = Advocate(email=data['email'], name=data['name'],
                          phone_number=data['phone_number'], created_on=date.today())
            adv.save()
            new_user = True
        orders = []
        for o in data['orders']:
            data1 = {
                'advocate': adv.id,
                'shirt': data['id'],
                'shirt_size': o,
                'order_date': date.today(),
                'order_price': data['order_price'],
                'order_uuid': order_uuid,
                'confirmed': False,
                'fulfilled': False
            }
            orders.append(data1)
        serializer = OrderSerializer(data=orders, many=True)
        if serializer.is_valid():

            text_response = texter.send_text(text_body, data['phone_number'])
            if text_response == "ERROR":
                if new_user:
                    adv.delete()
                return Response({"status": "error", "data": f"Problem with phone number: {data['phone_number']}"}, status=status.HTTP_400_BAD_REQUEST)
            
            adv.phone_number = data['phone_number']
            adv.save()

            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


def confirm_order(request, order_uuid):
    """
    Handling order confirmation via text url.
    """
    order_confirmed = False
    orders = Order.objects.filter(order_uuid=order_uuid)
    for order in orders:
        order.confirm()
        order.save()
        order_confirmed = True

        texter = Texter()
    if order_confirmed:
        texter.send_text(f"Order from {order.advocate} confirmed.", "9188845288")
    else:
        texter.send_text(f"Hmm weird order confirmation problem.", "9188845288")

    return HttpResponse('Thanks for confirming your order!')


def order_stats(request, template_name='order_stats.html'):
    """
    Stats for current order statuses.
    """

    shirts = Shirt.objects.all()
    orders = Order.objects.all()
    order_response = {}
    for shirt in shirts:
        if shirt.name not in order_response:
            order_response[shirt.name] = { 'freq': [0, 0, 0], 'sizes': { 'S': 0, 'M': 0, 'L': 0, 'XL': 0 } }

    raw_orders = {}
    for order in orders:

        if order.fulfilled:
            order_response[order.shirt.name]['freq'][2] += 1
        else:
            order_response[order.shirt.name]['freq'][1] += 1
            order_response[order.shirt.name]['sizes'][order.shirt_size] += 1
            if not order.confirmed:
                order_response[order.shirt.name]['freq'][0] += 1
            
            if order.shirt.name not in raw_orders:
                raw_orders[order.shirt.name] = {}

            if order.advocate.name not in raw_orders[order.shirt.name]:
                raw_orders[order.shirt.name][order.advocate.name] = {
                    "phone_number": order.advocate.phone_number,
                    "orders": [order.shirt_size],
                    "total_price": order.order_price
                }
            else:
                raw_orders[order.shirt.name][order.advocate.name]["orders"].append(order.shirt_size)
                raw_orders[order.shirt.name][order.advocate.name]["total_price"] += order.order_price
    return render(request, template_name, { "shirts": order_response, "raw_orders": raw_orders })

