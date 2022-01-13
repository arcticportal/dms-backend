from django.contrib.gis.db import models

from apps.utils.models import Place


class AdministrativeArea(Place):
    pass


class Country(AdministrativeArea):
    postal = models.CharField(max_length=16, null=True, blank=True)
    country_type = models.CharField(max_length=128, null=True, blank=True)
    fips_10 = models.CharField(max_length=4, null=True, blank=True)
    wikidata_id = models.CharField(max_length=16, null=True, blank=True)
    continent = models.CharField(max_length=128, null=True, blank=True)
    subregion = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = "country"
        verbose_name = "Country"
        verbose_name_plural = "Countries"
