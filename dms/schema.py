from typing import List

import strawberry
import strawberry_django

from apps.administrative_area.types import CountryType, StateType, CityType
from apps.civic_structure.types import BoatTerminalType, ScientificStationType


@strawberry.type
class Query:
    country: CountryType = strawberry_django.field()
    countries: List[CountryType] = strawberry_django.field()

    state: StateType = strawberry_django.field()
    states: List[StateType] = strawberry_django.field()

    boat_terminal: BoatTerminalType = strawberry_django.field()
    boat_terminals: List[BoatTerminalType] = strawberry_django.field()

    city: CityType = strawberry_django.field()
    cities: List[CityType] = strawberry_django.field()
    
    scientific_station: ScientificStationType = strawberry_django.field()
    scientific_stations: List[ScientificStationType] = strawberry_django.field()

schema = strawberry.Schema(query=Query)
