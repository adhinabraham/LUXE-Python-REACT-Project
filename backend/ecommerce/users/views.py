

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .models import MyUser
from .serializer import MyMobileserializer, MyUserSerializer
from django.contrib.auth.hashers import make_password
from os import chmod
import os
from django.http import Http404
from django.contrib import messages
from twilio.rest import Client
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .private import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_SERVICE_SID









# Create your views here.


# <-------------------------usersiginup view-------------------------->
class Signup(APIView):
    
    def post(self,request):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("saved ayyeee")
            return Response(serializer.data, status=status.HTTP_201_CREATED , )
         
        print("",serializer.errors)
        # response = JsonResponse(serializer.errors, status=500)
        return Response(serializer.errors,status=status.HTTP_502_BAD_GATEWAY)

   
class Otp(APIView):

    def get_mobile(self,num):
     try:
            return MyUser.objects.get(mobile_number=num)
     except MyUser.DoesNotExist:
            raise Http404 
   
    def post (self,request):
        print ("this is otp")
        mobile =request.data
        num=mobile['mobile_number']
        print(num)
        data=self.get_mobile(num)
   
        if data is not None:
           
            user_mobile='+91'+num
            print (user_mobile)
            account_sid = TWILIO_ACCOUNT_SID
            auth_token = TWILIO_AUTH_TOKEN
            Services=TWILIO_SERVICE_SID
            client = Client(account_sid, auth_token)
            verification = client.verify \
                .services(Services) \
                .verifications \
                .create(to=user_mobile, channel='sms')
            print(verification.status)
            messages.info(request,'Please enter the otp you have recieved on your mobile')
               
            return Response( status=status.HTTP_201_CREATED )
        
        return Response(status=status.HTTP_502_BAD_GATEWAY)


    #  number=mobile['mobile_number']
    #  print (mobile['mobile_number'])
    #  user_mobile='+91'+number
    #  print (user_mobile)
    #  account_sid = TWILIO_ACCOUNT_SID
    #  auth_token = TWILIO_AUTH_TOKEN
    #  Services=TWILIO_SERVICE_SID
    #  client = Client(account_sid, auth_token)
    #  verification = client.verify \
    #      .services(Services) \
    #      .verifications \
    #      .create(to=user_mobile, channel='sms')

    #  print(verification.status)
    #  messages.info(request,'Please enter the otp you have recieved on your mobile')
    #  return Response('double_varification.html')
     
class otpverification(APIView):
    def post(self,request):
        otp=request.data
        print (otp,"this is otp and and here ...")
        otpcode =otp['otp']
        number=otp['mobile_number']
        usermobile="+91"+number
        print(otpcode)
        # account_sid = os.environ['TWILIO_ACCOUNT_SID']
        # auth_token = os.environ['TWILIO_AUTH_TOKEN']
        account_sid=TWILIO_ACCOUNT_SID
        auth_token=TWILIO_AUTH_TOKEN
        Services=TWILIO_SERVICE_SID
        client = Client(account_sid, auth_token)

        verification_check = client.verify \
                                .services(Services) \
                                .verification_checks \
                                .create(to=usermobile, code=otpcode)

        print(verification_check.status)
        print ("this is otp verification")

        return Response(status=status.HTTP_202_ACCEPTED)



  
    
    # twilio code for otp generation
 

   

     







# {"username":"niyas",
# "password":"12345",
#  "mobile_number":"0000000000",
#  "email":"adhinabraham@gmail.com"}
# {"mobile_number":"7012682523"}
# {"otp":""}