import datetime
import random

from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from common import function

User = get_user_model()


def generate_otp():
    random_no = str(int(random.randint(1001, 9999)))
    return int(str(random_no)[0:4])


def prepare_message(otp):
    return "Otp for logging in meeting point is %s" %(otp)


class SendOtp(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        phone = request.data.get('phone')
        phone = function.normalise_phone(phone)
        otp = generate_otp()
        message = prepare_message(otp)
        code = "+91"
        phone = code + phone
        User.objects.filter(phone=phone).update(otp=otp, otp_sent_at = datetime.datetime.now())
        function.notify(phone, message)
        return {'success': True, 'message': "Otp sent successfully."}

# class VerifyOtp(APIView)
#     permission_classes = (AllowAny,)
#
#     def post(self, request):

