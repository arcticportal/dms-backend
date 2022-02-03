import strawberry_django
from strawberry_django import auto

from .models import BoatTerminal, ScientificStation

# -------------------------------------------------------------
# --------------------STRAWBERRY_FILTERS-----------------------


@strawberry_django.filters.filter(BoatTerminal, lookups=True)
class BoatTerminalFilter:
    name: auto


@strawberry_django.filters.filter(ScientificStation, lookups=True)
class ScientificStationFilter:
    name: auto


# -------------------------------------------------------------
# --------------------STRAWBERRY_ORDERS------------------------


@strawberry_django.ordering.order(BoatTerminal)
class BoatTerminalOrder:
    id: auto
    name: auto


@strawberry_django.ordering.order(ScientificStation)
class ScientificStationOrder:
    id: auto
    name: auto


# -------------------------------------------------------------
# --------------------STRAWBERRY_QUERY_TYPES-------------------


@strawberry_django.type(BoatTerminal, filters=BoatTerminalFilter, order=BoatTerminalOrder, pagination=True)
class BoatTerminalQuery:
    id: auto
    name: str
    url: str
    point: str


@strawberry_django.type(
    ScientificStation, filters=ScientificStationFilter, order=ScientificStationOrder, pagination=True
)
class ScientificStationQuery:
    id: auto
    name: str
    geonames_id: str
    whosonfirst_id: str
    wikidata_id: str
    country: str
    point: str
    science_station_type: str
