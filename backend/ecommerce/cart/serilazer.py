
from itertools import product
from rest_framework import serializers
from .models import Cart
from products.serilazer import MyproductSerializer
from users.serializer import  MyUser

class MycartSerializer(serializers.ModelSerializer):
    username=MyUser()
    products = serializers.CharField(source='product_id.productname')  
    image_url = serializers.ImageField(source='product_id.image')
    price=serializers.CharField(source='product_id.price')
    sub_total=serializers.CharField
    # photo_url = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)


    class Meta:
        model = Cart
        fields = ['username','products','product_stock','price','sub_total','image_url']




# class CarSerializer(serializers.ModelSerializer):
#     photo_url = serializers.SerializerMethodField()

#     class Meta:
#         model = Car
#         fields = ('id','name','price', 'photo_url') 

#     def get_photo_url(self, car):
#         request = self.context.get('request')
#         photo_url = car.photo.url
#         return request.build_absolute_uri(photo_url
   


