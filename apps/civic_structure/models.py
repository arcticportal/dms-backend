from django.contrib.gis.db import models

from apps.utils.models import Place


class CivicStructure(Place):
    pass

    class Meta:
        db_table = "civic_structure"
        verbose_name = "Civic structure"
        verbose_name_plural = "Civic structures"


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
