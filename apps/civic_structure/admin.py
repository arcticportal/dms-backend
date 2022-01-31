from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import BoatTerminal


@admin.register(BoatTerminal)
class AdminBoatTerminal(LeafletGeoAdmin):
    list_display = (
        "name",
        "url",
    )
    search_fields = ("name",)
