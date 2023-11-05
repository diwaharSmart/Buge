from django.utils.html import format_html
from django.contrib import admin
from location_tracker_client.models import *
# Register your models here.

class LocationInline(admin.TabularInline):
    model = Location
    extra = 0

class DeviceAdmin(admin.ModelAdmin):
    inlines = [LocationInline]
    list_display = ["device_id","name","model_name","sku","owner_name","map_link"]
    search_fields = ["device_id","sku","name"]

    def map_link(self, obj):
        return format_html("<a target="+"_blank"+" href="+"https://www.google.com/maps/search/"+str(obj.last_location)+">last location</a>")

    map_link.allow_tags = True
    map_link.short_description = 'Column description'







admin.site.register(Device,DeviceAdmin)
admin.site.register(Location)