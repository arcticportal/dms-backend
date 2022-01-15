# from django.contrib.gis.db import models

from apps.utils.models import Place


class Landform(Place):
    pass

    class Meta:
        db_table = "landform"


class Continent(Landform):
    pass

    class Meta:
        db_table = "continent"


class BodyOfWater(Landform):
    pass

    class Meta:
        db_table = "body_of_water"


class OceanBodyOfWater(BodyOfWater):
    pass

    class Meta:
        db_table = "ocean_body_of_water"
