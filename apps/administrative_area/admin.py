from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .forms import RawAdminForm
from .models import Country


@admin.register(Country)
class OSMCountry(LeafletGeoAdmin):
    list_display = (
        "name",
        "postal",
        "fips_10",
    )
    search_fields = ("name",)
    form = RawAdminForm
