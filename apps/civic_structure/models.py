from django.contrib.gis.db import models

from apps.administrative_area.models import Country, State
from apps.utils.models import Place


class CivicStructure(Place):
    pass

    class Meta:
        abstract = True


class AirportType(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = "airport_type"
        verbose_name = "Airport type"
        verbose_name_plural = "Airport types"

    def __str__(self):
        return self.name if self.name else ""


class Airport(CivicStructure):
    airport_type = models.ForeignKey(AirportType, null=True, blank=True, on_delete=models.SET_NULL)
    iata_code = models.CharField(max_length=16, null=True, blank=True)
    gps_code = models.CharField(max_length=16, null=True, blank=True)
    local_code = models.CharField(max_length=16, null=True, blank=True)
    elevation_ft = models.FloatField(null=True, blank=True)
    our_airports_id = models.IntegerField(null=True, blank=True)
    state = models.ForeignKey(State, null=True, blank=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "airport"
        verbose_name = "Airport"
        verbose_name_plural = "Airports"


class BoatTerminal(CivicStructure):
    pass

    class Meta:
        db_table = "boat_terminal"
        verbose_name = "Boat terminal"
        verbose_name_plural = "Boat terminals"


class ScientificStationType(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = "science_station_type"
        verbose_name = "Scientific station type"
        verbose_name_plural = "Scientific station types"

    def __str__(self):
        return self.name if self.name else ""


class ScientificStation(CivicStructure):
    geonames_id = models.CharField(max_length=16, null=True, blank=True)
    whosonfirst_id = models.CharField(max_length=16, null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL)
    science_station_type = models.ForeignKey(ScientificStationType, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "science_station"
        verbose_name = "Scientific station"
        verbose_name_plural = "Scientific stations"
