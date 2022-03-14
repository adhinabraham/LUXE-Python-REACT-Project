
from django.urls import path
from . import views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


urlpatterns = [
   
    path('siginup/',views. Signup.as_view()),
    path('otp/',views.Otp.as_view()),
    path('otpnumber/',views.otpverification.as_view()),
    path('user/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
