from django.urls import path
from . import views


urlpatterns = [
   
    path('products/',views.Addcart.as_view()),
]
