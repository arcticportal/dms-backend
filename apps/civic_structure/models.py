from django.contrib.gis.db import models

from apps.utils.models import Place


class CivicStructure(Place):
    pass

    class Meta:
        db_table = "civic_structure"


class Airport(CivicStructure):
    airport_type = models.CharField(max_length=16, null=True, blank=True)
    iata_code = models.CharField(max_length=16, null=True, blank=True)
    gps_code = models.CharField(max_length=16, null=True, blank=True)

    class Meta:
        db_table = "airport"


class BoatTerminal(CivicStructure):
    pass

    class Meta:
        db_table = "boat_terminal"
