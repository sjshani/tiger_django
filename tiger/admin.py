from django.contrib import admin

# Register your models here.

from .models import IncomingPallet
from .models import Location
from .models import WorkStation
from .models import Battery, BatteryTest, TigerEvent
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.db import models



class IncomingPalletAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "display_batteries"
        ]
    search_fields = list_display
    def display_batteries(self, obj):
         url = reverse('pallet_detail', kwargs={'serial_number': obj.serial_number})
         return mark_safe(f'<a href="{url}">{obj.serial_number}</a>')
    display_batteries.short_description = 'serial_number'
admin.site.register(IncomingPallet, IncomingPalletAdmin)

admin.site.register(Location)

class WorkStationAdmin(admin.ModelAdmin):
    list_display = [
        "host_name",
        "code",
        "location",
        "current_pallet"
        ]
admin.site.register(WorkStation, WorkStationAdmin)

class BatteryTestAdmin(admin.ModelAdmin):
    list_display = [
        "battery",
        "actual_voltage_reading",
        "cleaning_required",
        "workstation"
    ]
class BatteryTestInline(admin.TabularInline):
    model = BatteryTest
    extra = 0
    can_delete = False
    verbose_name = "Battery Test"
    verbose_name_plural = "Battery Tests"
    readonly_fields = ['actual_voltage_reading', 'scanned_voltage_reading', 'scanned_serial_number', 
                       'actual_serial_number', 'cleaning_required', 'location', 'workstation']
admin.site.register(BatteryTest, BatteryTestAdmin)
    
class BatteryAdmin(admin.ModelAdmin):
    list_display = [
        "serial_number",
        "incoming_pallet",
    ]
    readonly_fields = ['serial_number', 'incoming_pallet']
    inlines = [BatteryTestInline]
admin.site.register(Battery, BatteryAdmin)

admin.site.register(TigerEvent)
