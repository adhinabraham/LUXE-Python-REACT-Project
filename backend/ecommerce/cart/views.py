from ast import Delete
from multiprocessing import AuthenticationError
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from django.http import Http404
from rest_framework import viewsets
from .serilazer import MycartShowSerializer, CartSerializer
from django.shortcuts import get_object_or_404
from rest_framework. permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import BasicAuthentication

from .models import Cart
from products.models import Product


# Create your views here.
class Viewcart(APIView):

    def post(self, request):
        print("this is  view of cart ")
        data = request.data
        print("this is data api view")
        id = request.data.get("username")

        items = Cart.objects.filter(username=id)
        serilazer = MycartShowSerializer(
            items, many=True, context={'request': request})

        return Response(serilazer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        print("this is deleting item")
        item = Cart.objects.get(id=pk)
        item.delete()
        print("item deleted")
        return Response("deleted", status=status.HTTP_202_ACCEPTED)


class AddCart(APIView):

    def post(self, request):
        print("request come in add cart ")
        product_id = request.data["product_id"]
        user_id = request.data["username"]
        print (user_id)

        try:

            print(user_id)
            print(product_id)
            product_available = Cart.objects.get(
                product_id=product_id, username=user_id)
            print(product_available)
            print("priduct available, going to addd")
        except:
            print("product not availablale")
            print("new product is adding ")

            product = Product.objects.get(id=product_id)
            data = {"product_id": product_id, "username": user_id,"product_stock":1,"sub_total":product.price}

            serilazerproduct = CartSerializer(data=data)

            print(serilazerproduct)
            if serilazerproduct.is_valid():
                print("product is vaid ")
               
                serilazerproduct.save()

                return Response({"message": " new product is add to cart "})
            return Response({"message": " some error "})

        if product_available:
            print('product found, adding quantity')

            print(product_available.product_stock, "before adding")

            product_available.product_stock = product_available.product_stock+1
            product_available.sub_total = product_available.product_stock * \
                product_available.product_id.price
            product_available.save()
            print(product_available.product_stock, "after adding")
            return Response({'message': 'product qty added'})

    def patch(self,request):
        print("this is patch method")
        print(request.data)
        print("this is product data items")
        product_id=request.data["product_id"]
        userid=request.data["user_id"]
        action=request.data["action"]
        product_stock=request.data["product_stock"]
        print(product_id,userid,product_stock,action)
        product_item=Cart.objects.get(product_id=product_id,username=userid)
        print(product_item,"this is product item")

        if action =="add":
     
      
            
            print(product_item)
            print(product_item.product_stock,"product stock ")
            product_item.product_stock=product_item.product_stock+1
            product_item.sub_total= product_item.product_stock * product_item.product_id.price
            product_item.save()
            print(product_item.product_stock,"add stock")
            print("this is successfull compled ")
            return Response ("stock added")
        
        else:
           if product_item.product_stock >1:
              print(product_item.product_stock,"product stock ")
              product_item.product_stock=product_item.product_stock-1
              product_item.sub_total= product_item.product_stock * product_item.product_id.price
              product_item.save()
              print(product_item.product_stock,"add stock")
              print("this is succesfully decresed")
              return Response("stock decreased")

           else :
                return Response (" item can't removed ")

    def put(self, request ):
        print ("delete function in cart ")
        print(request.data)
        userid = request.data["userid"]
        print(userid)
        items = Cart.objects.filter(username=userid)
        items.delete()
        print("items all are deleted ")
        return Response(status=status.HTTP_204_NO_CONTENT) 

# {"product_id":28,"user_id":31,"product_stock":4,"action":"add"}



# class CartView(viewsets.ViewSet):

#     # def get_permissions(self):

#     #  if self.action == 'list':
#     #     permission_classes = [IsAuthenticated]
#     #     print("is authinecated")
#     #  else:
#     #     permission_classes = [IsAuthenticated]
#     #  return [permission() for permission in permission_classes]

#     def list(self, request):
#         print(request.data, "this is post")

#         queryset = Cart.objects.all()
#         serializer = CartSerializer(
#             queryset, many=True, context={'request': request})
#         return Response(serializer.data)

#     # def retrieve(self, request, pk=None):
#     #     print (request.data,'this is form data')

#     #     queryset = Cart.objects.all()
#     #     items = get_object_or_404(queryset, pk=pk)
#     #     serializer = CartSerializer(items)
#     #     return Response(serializer.data)

#     def destroy(self, request, pk=None):
#         print("this is deleting function ")
#         queryset = get_object_or_404(Cart, id=pk).delete()
#         return Response({'message': 'delete success'})

#     def create(self, request):
#         print('add to cart in viewset')
#         print(request.data)
#         product = request.data["product_id"]
#         item = Cart.objects.filter(id=product)
#         print(item)

#         # serializer = CartSerializer(data=request.data)
#         # print(serializer)
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     print("data is added  to cart")
#         #     return Response({'message':'success','data':serializer.data})
#         # return Response({'message':'error','data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#         return Response("this is product item ")


# {"product_id":{"product":27},"username":31}
