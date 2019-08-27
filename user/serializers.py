from rest_framework import serializers
from .models import *


class SignupSerializer(serializers.ModelSerializer):
    model = User
    fields = ('first_name', 'last_name', 'phone')

