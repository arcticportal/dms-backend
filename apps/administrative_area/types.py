import strawberry_django
from .models import Country

@strawberry_django.type(Country)
class Country:
    name: str
    fips_10: str