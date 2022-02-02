import strawberry_django
from strawberry_django import auto

from .models import BoatTerminal, ScientificStation


@strawberry_django.filters.filter(BoatTerminal, lookups=True)
class BoatTerminalFilter:
    name: auto


@strawberry_django.ordering.order(BoatTerminal)
class BoatTerminalOrder:
    id: auto
    name: auto


@strawberry_django.type(BoatTerminal, filters=BoatTerminalFilter, order=BoatTerminalOrder, pagination=True)
class BoatTerminalType:
    id: auto
    name: str
    url: str
    point: str


@strawberry_django.filters.filter(ScientificStation, lookups=True)
class ScientificStationFilter:
    name: auto


@strawberry_django.ordering.order(ScientificStation)
class ScientificStationOrder:
    id: auto
    name: auto


@strawberry_django.type(ScientificStation, filters=ScientificStationFilter, order=ScientificStationOrder, pagination=True)
class ScientificStationType:
    id: auto
    name: str
    geonames_id: str
    whosonfirst_id: str
    wikidata_id: str
    country: str
    point: str
    science_station_type: str
