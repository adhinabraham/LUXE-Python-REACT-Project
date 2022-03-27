from itertools import product

from urllib.parse import uses_relative
from wsgiref.util import request_uri
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404 
from .serializer import OrderAddressSerializer,OrderSerializer,OrderAdminserializer,OrdernumberSerializer
from .models import Address, Order,Ordernumber
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from cart.models import Cart

import random
import string
import datetime
import itertools





# Create your views here.


class OrderAddress(APIView):

        def get(self,request):
            print("this is get")
            data=Address.objects.all()
            print("pro")
            seriail=OrderAddressSerializer(data,many=True)
            return Response(seriail.data,status=status.HTTP_200_OK)

        def post(self,request):
            serializer = OrderAddressSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print("saved ayyeee")
                return Response(serializer.data, status=status.HTTP_201_CREATED , )
            
            print("",serializer.errors)
           
            return Response(serializer.errors,status=status.HTTP_502_BAD_GATEWAY)




class ordernumber_generation(APIView):
    def get(self,request):
        print("this is otp")
        yr                  = int(datetime.date.today().strftime('%Y'))
        dt                  = int(datetime.date.today().strftime('%d'))
        mt                  = int(datetime.date.today().strftime('%m'))
        d                   = datetime.date(yr,mt,dt)
        current_date        = d.strftime("%Y%m%d")
        orderno = Ordernumber()

        orderno.save()
        orderno.order_no       = current_date + str(orderno.id)
        orderno.save()
        print(orderno)

        
        return Response({"num":orderno.order_no})
        

class Orderplaced(APIView):
    def post (self,request):
        print("order palced ")
       
        userid=request.data["username"]
        ordernum=request.data["order_number"]
        orderid = Ordernumber.objects.get(order_no=ordernum)
        Idorder=orderid.id
       
        request.data['order_number']=Idorder

      
       
        items=Cart.objects.filter(username=userid)
        order=Order()

        for i in items:
           print(i.product_id_id)
           request.data["product"]=i.product_id_id
           request.data["product_stock"]=i.product_stock
           print("this is product assigned")
           print (request.data,"this is request.data")
           seril=OrderSerializer(data=request.data)
           if seril.is_valid(raise_exception=True):
               seril.save()
               print("this is porduct")
           else :
               return Response ("this is not a valid data")
          
        print("for loop is completed")
        return Response ({"status":"true"})

    def get(self,request):
            print("this is get")
            data=Order.objects.all()
            print("pro")
            seriail=OrderAdminserializer(data,many=True,context={'request': request})
            return Response(seriail.data,status=status.HTTP_200_OK)
    def patch(self,request):
        print("this is patch ")
        orderid=request.data["orderid"]
        productid=request.data["productid"]
        orderstatus=request.data["status"]
        item=Order.objects.get(order_number=orderid,product=productid)

        item.status=orderstatus
        item.save()
        serial = OrderSerializer(data=item)
        print(serial)
        return Response (" saved ")



class Userorder(APIView):
   
    def post(self, request):
       
        username= request.data["username"]
        data = Order.objects.filter(username=username)
        useritems = OrderAdminserializer(data, many=True,context={'request':request})
        return Response (useritems.data)


class ordernumberlist(APIView):

    def post(self, request):
        print ("ordre number function")

        username = request.data["username"]
        data = Order.objects.filter(username=username)
        print(type(data))
        print (data)
        useritems = OrdernumberSerializer(
            data, many=True,)
       
        return Response(useritems.data)


      
        # return Response ({"data":"saved"})

#  {"status":"item_shipped","orderid":"2022032169","productid":"29"}
#instance.email = validated_data.get('email', instance.email)


# # {"userid":"31","address":3,"payment_method":"COD","order_number":2022201} 




        

           



       
            



       
        # return Response ({"data":"notsaved"})




        
 



# class Ordermanage(APIView):
#{"userid":31}
    

#  {"full_name":"zayan malik","mobile":"7012682523","state":"kerala","city":"kalladikode","district":"palakkad","address_line1":"puthenparambil"}