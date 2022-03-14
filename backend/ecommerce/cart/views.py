from multiprocessing import AuthenticationError
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from django.http import Http404
from rest_framework import viewsets
from .serilazer import MycartSerializer
from django.shortcuts import get_object_or_404
from rest_framework. permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import  BasicAuthentication

from .models import Cart
from products.models import Product





# Create your views here.
class Viewcart(APIView):
    
    def post (self,request):
        data=request.data
        print ("this is data api view")
        id=request.data.get("username")
        

        items=Cart.objects.filter(username=id)
        serilazer=MycartSerializer(items,many=True, context={'request': request})
        print(serilazer.data)

      
        return Response(serilazer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        

    # {"product_id":27,
    # "username":'sayan',
    # }



class CartView(viewsets.ViewSet):


    # def get_permissions(self):
   
    #     if self.action == 'list':
    #         permission_classes = [IsAuthenticated]
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]






    def list(self, request):
        print (request.data,"this is post")

        queryset = Cart.objects.all()
        serializer = MycartSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)



    def retrieve(self, request, pk=None):
        print (request.data,'this is form data')

        queryset = Cart.objects.all()
        items = get_object_or_404(queryset, pk=pk)
        serializer = MycartSerializer(items)
        return Response(serializer.data)


    # def post(self, request, pk=None):
    #     # permission_classes = [IsAuthenticated]
    #     # authentication_classes=[BasicAuthentication]
    #     print("this is retrive")
    #     print(self.request.user)
    #     queryset = Cart.objects.filter(username=request.user)
    #     user = get_object_or_404(queryset, )
    #     serializer = MycartSerializer(user)
    #     return Response(serializer.data)




    # def list(self, request,pk):
    #     print (pk)
    #     print("this is request",request.user.id)
    #     queryset = Cart.objects.filter(id=pk)
    #     serializer = MycartSerializer(queryset,many=True , context={'request': request})
    #     return Response(serializer.data)

        # queryset = Cart.objects.all()
        # user = get_object_or_404(queryset, id=pk)
        # serializer = MycartSerializer(user)
        # return Response(serializer.data)



    def create(self, request):
        print('add to cart in viewset')
        print(request.data)
     
        serializer = MycartSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            print("data is added  to cart")
            return Response({'message':'success','data':serializer.data})
        return Response({'message':'error','data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)







# {"product_id":{"product":27},"username":31}