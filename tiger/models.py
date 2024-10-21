from django.db import models

# Create your models here.
class Location(models.Model):
    class Meta:
        db_table = "locations"
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30)

class IncomingPallet(models.Model):
    class Meta:
        db_table = "incoming_pallets"
    serial_number = models.CharField(max_length=30)
    def __str__(self):
        return self.serial_number

class Battery(models.Model):
    class Meta:
        db_table = "batteries"
        verbose_name = "Battery"
        
    incoming_pallet = models.ForeignKey(IncomingPallet, on_delete=models.CASCADE, related_name ='batteries')
    serial_number = models.CharField(max_length=30)
    def __str__(self):
        return self.serial_number
    
class WorkStation(models.Model):
    class Meta:
        db_table = "workstations"
    host_name =  models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)
    #battery_test = models.ForeignKey(BatteryTest, on_delete=models.CASCADE)
    current_pallet = models.ForeignKey(IncomingPallet, on_delete = models.CASCADE, null=True)
    def __str__(self):
        return self.host_name


class BatteryTest(models.Model):
    class Meta:
        db_table = "battery_tests"
    battery = models.ForeignKey(Battery, on_delete=models.CASCADE)
    workstation = models.ForeignKey(WorkStation, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    scanned_serial_number = models.CharField(max_length=50, null=True)
    actual_serial_number  = models.CharField(max_length=50, null=True)
    scanned_voltage_reading = models.FloatField(null=True)
    actual_voltage_reading = models.FloatField(null=True)
    cleaning_required = models.BooleanField(null=True)
    initial_image = models.BinaryField(null=True)
    serial_number_image = models.BinaryField(null=True)
    voltage_reading_image = models.BinaryField(null=True)
    



EVENT_TYPES = [
    ("INFO", "Information"),
    ("WARNING", "Warning"),
    ("ERROR", "Error"),
]

class TigerEvent(models.Model):
    class Meta:
        db_table = "events"
       
    def __str__(self):
        return self.description

    severity = models.CharField(max_length=50, choices=EVENT_TYPES)
    description = models.CharField(max_length=100)
    information = models.TextField(blank=True, null=True)

