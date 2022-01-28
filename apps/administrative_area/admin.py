from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .forms import RawAdminForm
from .models import Country


@admin.register(Country)
class OSMCountry(LeafletGeoAdmin):
    list_display = (
        "name",
        "fips_10",
        "iso2",
        "iso3",
    )
    search_fields = ("name",)
    list_filter = ("continent", "country_type", "subregion")
    form = RawAdminForm
