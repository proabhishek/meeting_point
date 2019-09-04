from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Meeting)
admin.site.register(Invitation)
admin.site.register(Address)