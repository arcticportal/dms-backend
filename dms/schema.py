import strawberry
from typing import List
from apps.administrative_area.types import Country

@strawberry.type
class Query:
    fruits: List[Country]

schema = strawberry.Schema(query=Query)