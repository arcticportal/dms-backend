from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Airport, BoatTerminal, ScientificStation


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


@admin.register(Airport)
class AdminAirport(LeafletGeoAdmin):
    fields = (
        "name",
        "point",
        "url",
        "wikipedia_url",
        "iata_code",
        "gps_code",
        "local_code",
        "airport_type",
        "elevation_ft",
        "our_airports_id",
        "country",
        "state",
    )
    list_display = (
        "name",
        "iata_code",
        "country",
        "state",
    )
    search_fields = (
        "name",
        "iata_code",
    )
    list_filter = (
        "airport_type",
        "country",
    )
