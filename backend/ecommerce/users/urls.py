
from django.urls import path
from . import views


urlpatterns = [
   
    path('siginup/',views. Signup.as_view()),
    path('otp/',views.Otp.as_view()),
    path('otpnumber/',views.otpverification.as_view()),
    
]
