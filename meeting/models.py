from django.db import models
from user.models import User



class Meeting(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=500, null=True, blank=True)
    start_date_time = models.DateTimeField()
    duration = models.PositiveSmallIntegerField()
    hosted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Invitation(models.Model):
    invite_status = {
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('pending', 'Pending')
    }
    invitor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="inviter")
    invited = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invited')
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    status = models.CharField(choices=invite_status, default='pending', max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Address(models.Model):
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
