from django.urls import path
from . import views




urlpatterns = [
   
    path('orderaddress/',views.OrderAddress.as_view()),
    path('ordernumber/',views.ordernumber_generation.as_view()),
    path('orderplaced/',views.Orderplaced.as_view()),
    path('userorder/', views.Userorder.as_view()),
    path('orderid/', views.ordernumberlist.as_view()),

    # path('showproduct/<int:pk>',views.showproduct.as_view()),
]