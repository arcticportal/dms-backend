import strawberry
from typing import List
from apps.administrative_area.types import Country
import strawberry_django


@strawberry.type
class Query:
    countries: List[Country] = strawberry_django.field()

schema = strawberry.Schema(query=Query)
