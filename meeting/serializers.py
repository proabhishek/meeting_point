from rest_framework import serializers
from .models import *


class MeetingSerializer(serializers.ModelSerializer):
    # start_date_time = serializers.DateTimeField(read_only=True)
    hosted_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
      model = Meeting
      fields = '__all__'


class InvitationSerializer(serializers.ModelSerializer):
    inviter = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    class Meta:
      model = Invitation
      fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    class Meta:
        model = Address
        fields = '__all__'