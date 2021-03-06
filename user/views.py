import datetime
import random

from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Create your views here.
from django.utils import timezone
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from meeting_point.response import api_response
from rest_framework import generics
from .serializers import *
from .models import *
from common import function

User = get_user_model()


def generate_otp():
    random_no = str(int(random.randint(1001, 9999)))
    return int(str(random_no)[0:4])


def prepare_message(otp):
    return "Otp for logging in meeting point is %s" %(otp)


def send_message(phone, user):
    phone = function.normalise_phone(phone)
    otp = generate_otp()
    message = prepare_message(otp)
    code = "+91"
    phone = code + phone
    user.otp = otp
    user.otp_sent_at = timezone.now()
    user.save()
    function.notify(phone, message)


def profile_complete(user):
    return True if user.first_name else False


# class SendOtp(APIView):
#     permission_classes = (AllowAny,)
#
#     @api_response
#     def post(self, request):
#         phone = request.data.get('phone')
#         user = User.objects.get(phone=phone)
#         send_message(phone, user)
#         return {'success': True, 'message': "Otp sent successfully"}


class VerifyOtp(APIView):
    permission_classes = (AllowAny,)

    @api_response
    def post(self, request):
        phone = request.data.get('phone')
        otp = request.data.get('otp')
        user = User.objects.get(phone=phone)
        if user.otp == otp:
            token = Token.objects.create(user=user)
            return {'success': True, 'message': "Correct Otp", 'data': {"auth-token": token.key}}
        else:
            return {'success': False, 'message': "Wrong Otp"}


# class SignUpView(generics.CreateAPIView):
#     import pdb
#     pdb.set_trace()
#     queryset = User.objects.all()
#     serializer_class = SignupSerializer
#     permission_classes = [AllowAny]

# class SignUpView(APIView):
#     permission_classes = (AllowAny,)
#
#     @api_response
#     def post(self, request):
#         phone = request.data.get('phone')
#         first_name = request.data.get('first_name')
#         last_name = request.data.get('last_name')
#
#         user = User.objects.create(first_name= first_name, last_name=last_name, phone=phone)
#         if user:
#             return {'success': True, 'message': "User Created"}
#         else:
#             return {'success': False, 'message': "User couldnot be created"}


class Login(APIView):
    permission_classes = (AllowAny,)
    @api_response
    def post(self, request):
        phone = request.data.get('phone','')
        first_name = request.data.get('first_name', '')
        last_name = request.data.get('last_name', '')
        if first_name:
            user = User.objects.get_or_create(phone=phone, first_name=first_name, last_name=last_name)
        else:
            user = User.objects.get_or_create(phone=phone)
        if user:
            send_message(phone, user[0])
            return {'success': 1, 'message': 'Otp sent Successfully'}
        else:
            return {'success': 0, 'errors': user.objects.errors}


class Logout(APIView):
    # permission_classes = (Authenticated,)
    @api_response
    def delete(self, request):
        try:
            request.user.auth_token.delete()
            return {'success': True, 'message': 'Logout out Successfully'}
        except Exception as e:
            return {'success': False, 'error': 'Server Error'}

