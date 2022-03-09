from django.urls import path
from . import views


urlpatterns = [
   
    path('userlists/',views.Login.as_view()),
    path('useredit/<int:pk>',views.Useredit.as_view()),
    path('category/',views.Category.as_view()),
    path('product/',views.Product.as_view()),
    path('productdelete/<int:pk>',views.productdelete.as_view()),
   
]
