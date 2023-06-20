from django.contrib import admin

# Register your models here.
from .models import MyProfile,orders

admin.site.register(MyProfile)
admin.site.register(orders)