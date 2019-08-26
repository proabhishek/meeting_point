from django.urls import path, include
from .views import *

urlpatterns = [
    path('sendotp', SendOtp.as_view(), name='send-otp'),

]