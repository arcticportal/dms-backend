import strawberry_django
from strawberry_django import auto

from .models import BoatTerminal


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
