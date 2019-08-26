from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils import timezone


class UserManager(BaseUserManager):

  def _create_user(self, phone,  password, is_staff, is_superuser, **extra_fields):
    now = timezone.now()

    user = self.model(phone=phone,
             is_staff=is_staff, is_active=False,
             is_superuser=is_superuser, last_login=now,
             date_joined=now, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, phone, password=None, **extra_fields):
    return self._create_user(phone, password, False, False,
                 **extra_fields)

  def create_superuser(self, phone, password=None, **extra_fields):
    user =  self._create_user(phone, password, True, True,
                               **extra_fields)
    user.is_active=True
    user.save(using=self._db)
    return user


class User(AbstractUser):
    username = None
    # first_name = models.CharField(max_length=30, null=True, blank=True)
    # last_name = models.CharField(max_length=150,null=True, blank=True)
    phone = models.CharField(max_length=18, unique=True)
    otp = models.IntegerField(null=True, blank=True)
    otp_sent_at = models.DateTimeField(null=True, blank=True)
    self_signed_up = models.BooleanField(default=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'phone'
    objects = UserManager()

    class Meta:
        ordering = ['-id']
        db_table = 'User'




