from typing import List

import strawberry
import strawberry_django

from apps.administrative_area.types import Country


@strawberry.type
class Query:
    country: Country = strawberry_django.field()
    countries: List[Country] = strawberry_django.field()


schema = strawberry.Schema(query=Query)
