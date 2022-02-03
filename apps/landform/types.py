import strawberry_django
from strawberry_django import auto

from .models import BodyOfWater

# -------------------------------------------------------------
# --------------------STRAWBERRY_FILTERS-----------------------


@strawberry_django.filters.filter(BodyOfWater, lookups=True)
class BodyOfWaterFilter:
    name: auto
    body_of_water_type: auto


# -------------------------------------------------------------
# --------------------STRAWBERRY_ORDERS------------------------


@strawberry_django.ordering.order(BodyOfWater)
class BodyOfWaterOrder:
    id: auto
    name: auto


# -------------------------------------------------------------
# --------------------STRAWBERRY_QUERY_TYPES-------------------


@strawberry_django.type(BodyOfWater, filters=BodyOfWaterFilter, order=BodyOfWaterOrder, pagination=True)
class BodyOfWaterQuery:
    id: auto
    name: str
    geometry: str
    body_of_water_type: str
    natural_earth_id: str
    wikidata_id: str
