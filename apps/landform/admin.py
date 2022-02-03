from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import BodyOfWater, BodyOfWaterType


@admin.register(BodyOfWaterType)
class AdminBodyOfWaterType(LeafletGeoAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(BodyOfWater)
class AdminBodyOfWater(LeafletGeoAdmin):
    fields = ("name", "geometry", "wikidata_id", "body_of_water_type", "natural_earth_id")
    list_display = ("name", "wikidata_id")
    search_fields = ("name",)
    list_filter = ("body_of_water_type",)
