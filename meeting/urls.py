from django.urls import path

from .views import *

urlpatterns = [
    path('meeting/', MeetingCreateView.as_view(), name='meeting-create'),
    path('meeting/<int:pk>', MeetingCreateView.as_view(), name='meeting-update'),
    path('invitation', MeetingCreateView.as_view(), name='invitation-create'),
    path('invitation/<int:pk>', MeetingCreateView.as_view(), name='invitation-update'),
    path('address/', MeetingCreateView.as_view(), name='address-create'),
    path('address/<int:pk>', MeetingCreateView.as_view(), name='address-update'),
]