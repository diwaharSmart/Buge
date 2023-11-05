from django.db import models
import uuid

# Create your models here.
STATUS = (
    ("running","running"),
    ("uninstall","uninstall"),
)
class Device(models.Model):
    device_id     = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name          = models.CharField(max_length=255,blank=True,null=True)
    model_name    = models.CharField(max_length=255,blank=True,null=True)
    owner_name    = models.CharField(max_length=255,blank=True,null=True)
    sku    = models.CharField(max_length=255,blank=True,null=True)
    manfacturer    = models.CharField(max_length=255,blank=True,null=True)
    last_location = models.CharField(blank=True,null=True,max_length=255)
    status        = models.CharField(max_length=255,default="running",choices=STATUS)


LOCATION_MODE =(
    ("ip","ip"),
    ("live","live"),
)

class Location(models.Model):
    device        = models.ForeignKey("Device",on_delete=models.CASCADE,blank=True,null=True)
    location_mode = models.CharField(default="ip",max_length=255,choices=LOCATION_MODE)
    latitude      = models.CharField(blank=True,null=True,max_length=255)
    longitude     =  models.CharField(blank=True,null=True,max_length=255)
    ip_address    =  models.CharField(blank=True,null=True,max_length=255)
    city    =  models.CharField(blank=True,null=True,max_length=255)
    state    =  models.CharField(blank=True,null=True,max_length=255)
    country    =  models.CharField(blank=True,null=True,max_length=255)
    timestamp  =models.DateTimeField(auto_now_add=True)






