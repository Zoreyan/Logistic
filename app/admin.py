from django.contrib import admin
from .models import *

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ('plate_number',)


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'origin', 'destination')