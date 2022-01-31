from typing import List

import strawberry
import strawberry_django

from apps.administrative_area.types import CountryType, StateType


@strawberry.type
class Query:
    country: CountryType = strawberry_django.field()
    countries: List[CountryType] = strawberry_django.field()
    state: StateType = strawberry_django.field()
    states: List[StateType] = strawberry_django.field()


schema = strawberry.Schema(query=Query)
