from django.contrib.gis.db import models

from apps.utils.models import Place


class Landform(Place):
    pass

    class Meta:
        abstract = True


class Continent(Landform):
    pass

    class Meta:
        db_table = "continent"
        verbose_name = "Continent"
        verbose_name_plural = "Continents"


class BodyOfWaterType(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = "body_of_water_type"
        verbose_name = "Body of water type"
        verbose_name_plural = "Body of water types"

    def __str__(self):
        return self.name if self.name else ""


class BodyOfWater(Landform):
    body_of_water_type = models.ForeignKey(BodyOfWaterType, null=True, blank=True, on_delete=models.SET_NULL)
    natural_earth_id = models.CharField(max_length=16, null=True, blank=True)

    class Meta:
        db_table = "body_of_water"
        verbose_name = "Body of water"
        verbose_name_plural = "Bodies of water"
