from django.contrib import admin
from .models import Order, Car, Status

admin.site.register(Order)
admin.site.register(Car)
admin.site.register(Status)