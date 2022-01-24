# from django.contrib.gis.db import models

from apps.utils.models import Place


class Landform(Place):
    pass

    class Meta:
        db_table = "landform"
        verbose_name = "Landform"
        verbose_name_plural = "Landforms"


class Continent(Landform):
    pass

    class Meta:
        db_table = "continent"
        verbose_name = "Continent"
        verbose_name_plural = "Continents"


class BodyOfWater(Landform):
    pass

    class Meta:
        db_table = "body_of_water"
        verbose_name = "Body of water"
        verbose_name_plural = "Bodies of water"


class OceanBodyOfWater(BodyOfWater):
    pass

    class Meta:
        db_table = "ocean_body_of_water"
        verbose_name = "Ocean"
        verbose_name_plural = "Oceans"
