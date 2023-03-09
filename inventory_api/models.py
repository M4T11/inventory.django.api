from django.db import models

# Create your models here.

class LocationModel(models.Model):
    location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, default=None, unique=True)


class ProducerModel(models.Model):
    producer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, default=None, unique=True)


class CategoryModel(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, default=None, unique=True)

class EanDeviceModel(models.Model):
    ean_device_id = models.AutoField(primary_key=True)
    ean = models.CharField(max_length=50, blank=False, default=None, unique=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT)
    producer = models.ForeignKey(ProducerModel, on_delete=models.PROTECT)
    model = models.CharField(max_length=255)

class DeviceModel(models.Model):
    device_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=10000)
    ean_device = models.ForeignKey(EanDeviceModel, on_delete=models.PROTECT)
    quantity = models.IntegerField(blank=False, default=None)
    condition = models.CharField(max_length=255, blank=False, default=None)
    status = models.CharField(max_length=255, blank=False, default=None)
    date_added = models.DateField(blank=False, default=None)
    qr_code = models.CharField(max_length=255, blank=False, default=None)
    returned = models.BooleanField(default=False)

class DeviceHistoryModel(models.Model):
    history_id = models.AutoField(primary_key=True)
    event = models.CharField(max_length=255)
    device = models.ForeignKey(DeviceModel, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)









