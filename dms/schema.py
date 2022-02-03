from typing import List

import strawberry
import strawberry_django

from apps.administrative_area.types import CityQuery, CountryQuery, StateQuery
from apps.civic_structure.types import (AirportQuery, BoatTerminalQuery,
                                        ScientificStationQuery)
from apps.landform.types import BodyOfWaterQuery


@strawberry.type
class Query:
    # administrative_area
    country: CountryQuery = strawberry_django.field()
    countries: List[CountryQuery] = strawberry_django.field()

    state: StateQuery = strawberry_django.field()
    states: List[StateQuery] = strawberry_django.field()

    city: CityQuery = strawberry_django.field()
    cities: List[CityQuery] = strawberry_django.field()

    # civic_structure
    boat_terminal: BoatTerminalQuery = strawberry_django.field()
    boat_terminals: List[BoatTerminalQuery] = strawberry_django.field()

    airport: AirportQuery = strawberry_django.field()
    airports: List[AirportQuery] = strawberry_django.field()

    scientific_station: ScientificStationQuery = strawberry_django.field()
    scientific_stations: List[ScientificStationQuery] = strawberry_django.field()

    # landform
    body_of_water: BodyOfWaterQuery = strawberry_django.field()
    bodies_of_water: List[BodyOfWaterQuery] = strawberry_django.field()


schema = strawberry.Schema(query=Query)
