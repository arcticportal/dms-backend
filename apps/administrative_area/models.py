from django.contrib.gis.db import models

from apps.utils.models import Place
from apps.landform.models import Continent


class AdministrativeArea(Place):
    pass

    class Meta:
        abstract = True


class Subregion(models.Model):
    name = models.CharField(max_length=1024, null=True, blank=True)

    class Meta:
        db_table = "subregion"
        verbose_name = "Subregion"
        verbose_name_plural = "Subregions"

    def __str__(self):
        return self.name


class CountryType(models.Model):
    name = models.CharField(max_length=1024, null=True, blank=True)

    class Meta:
        db_table = "country_type"
        verbose_name = "Country Type"
        verbose_name_plural = "Country types"

    def __str__(self):
        return self.name


class Country(AdministrativeArea):
    postal = models.CharField(max_length=16, null=True, blank=True)
    country_type = models.ForeignKey(CountryType, null=True, blank=True, on_delete=models.SET_NULL)
    fips_10 = models.CharField(max_length=4, null=True, blank=True)
    continent = models.ForeignKey(Continent, null=True, blank=True, on_delete=models.SET_NULL)
    subregion = models.ForeignKey(Subregion, null=True, blank=True, on_delete=models.SET_NULL)
    iso2 = models.CharField(max_length=3, null=True, blank=True)
    iso3 = models.CharField(max_length=3, null=True, blank=True)

    class Meta:
        db_table = "country"
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class StateType(models.Model):
    name = models.CharField(max_length=1024, null=True, blank=True)

    class Meta:
        db_table = "state_type"
        verbose_name = "State Type"
        verbose_name_plural = "State types"

    def __str__(self):
        return self.name if self.name else ""


class State(AdministrativeArea):
    adm1_code = models.CharField(max_length=16, null=True, blank=True)
    iso_3166_1_2 = models.CharField(max_length=16, null=True, blank=True)
    fips = models.CharField(max_length=16, null=True, blank=True)
    state_type = models.ForeignKey(StateType, null=True, blank=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL)

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
