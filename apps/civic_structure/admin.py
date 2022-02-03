from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import BoatTerminal, ScientificStation


@admin.register(BoatTerminal)
class AdminBoatTerminal(LeafletGeoAdmin):
    list_display = (
        "name",
        "url",
    )
    search_fields = ("name",)


@admin.register(ScientificStation)
class AdminScientificStation(LeafletGeoAdmin):
    list_display = ("name", "country", "geonames_id", "wikidata_id")
    search_fields = ("name",)
    list_filter = ("science_station_type",)
