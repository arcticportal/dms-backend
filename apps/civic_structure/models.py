from django.contrib.gis.db import models

from apps.administrative_area.models import Country
from apps.utils.models import Place


class CivicStructure(Place):
    pass

    class Meta:
        abstract = True


class Airport(CivicStructure):
    airport_type = models.CharField(max_length=16, null=True, blank=True)
    iata_code = models.CharField(max_length=16, null=True, blank=True)
    gps_code = models.CharField(max_length=16, null=True, blank=True)

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
