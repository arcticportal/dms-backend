import strawberry_django
from strawberry_django import auto

from apps.administrative_area.models import Country


@strawberry_django.filters.filter(Country, lookups=True)
class CountryFilter:
    id: auto
    name: auto


@strawberry_django.ordering.order(Country)
class CountryOrder:
    id: auto
    name: auto


@strawberry_django.type(Country, filters=CountryFilter, order=CountryOrder, pagination=True)
class Country:
    id: auto
    name: auto
    mpoly: str
    fips_10: str
    continent: str
