
from users.models import MyUser
from products.models import category,Product
from rest_framework import serializers
from rest_framework.authentication import authenticate
class MyAdminserializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'


class Mycategory (serializers.ModelSerializer):
    class Meta:
        model = category
        fields ='__all__'

class Myproduct(serializers.ModelSerializer):
   
    class Meta:
        model = Product
        fields='__all__' 

      
