from django.contrib import admin

from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop
from leaflet.admin import LeafletGeoAdmin

@admin.register(Shop)
class ShopAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')
