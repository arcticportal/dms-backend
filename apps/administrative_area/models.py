from django.contrib.gis.db import models

from apps.utils.models import Place


class AdministrativeArea(Place):
    pass

    class Meta:
        db_table = "administrative_area"


class Country(AdministrativeArea):
    postal = models.CharField(max_length=16, null=True, blank=True)
    country_type = models.CharField(max_length=128, null=True, blank=True)
    fips_10 = models.CharField(max_length=4, null=True, blank=True)
    continent = models.CharField(max_length=128, null=True, blank=True)
    subregion = models.CharField(max_length=128, null=True, blank=True)
    iso2 = models.CharField(max_length=3, null=True, blank=True)
    iso3 = models.CharField(max_length=3, null=True, blank=True)

    class Meta:
        db_table = "country"
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class State(AdministrativeArea):
    adm1_code = models.CharField(max_length=16, null=True, blank=True)
    iso_3166_1_2 = models.CharField(max_length=16, null=True, blank=True)
    state_type = models.CharField(max_length=16, null=True, blank=True)

    class Meta:
        db_table = "state"
        verbose_name = "State"
        verbose_name_plural = "States"


class City(AdministrativeArea):
    adm1_code = models.CharField(max_length=16, null=True, blank=True)
    iso_3166_1_2 = models.CharField(max_length=16, null=True, blank=True)
    state_type = models.CharField(max_length=16, null=True, blank=True)
    fips = models.CharField(max_length=16, null=True, blank=True)

    class Meta:
        db_table = "city"
        verbose_name = "City"
        verbose_name_plural = "Cities"
