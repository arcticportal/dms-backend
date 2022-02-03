import strawberry_django
from strawberry_django import auto

from apps.administrative_area.models import City, Country, State

# -------------------------------------------------------------
# --------------------STRAWBERRY_FILTERS-----------------------


@strawberry_django.filters.filter(Country, lookups=True)
class CountryFilter:
    name: auto
    iso2: auto
    iso3: auto


@strawberry_django.filters.filter(State, lookups=True)
class StateFilter:
    name: auto
    country: auto


@strawberry_django.filters.filter(City, lookups=True)
class CityFilter:
    name: auto
    country: auto


# -------------------------------------------------------------
# --------------------STRAWBERRY_ORDERS------------------------


@strawberry_django.ordering.order(Country)
class CountryOrder:
    id: auto
    name: auto
    iso2: auto
    iso3: auto


@strawberry_django.ordering.order(State)
class StateOrder:
    id: auto
    name: auto


@strawberry_django.ordering.order(City)
class CityOrder:
    id: auto
    name: auto


# -------------------------------------------------------------
# --------------------STRAWBERRY_QUERY_TYPES-------------------


@strawberry_django.type(Country, filters=CountryFilter, order=CountryOrder, pagination=True)
class CountryQuery:
    id: auto
    name: auto
    postal: str
    country_type: str
    fips_10: str
    geometry: str
    continent: str
    subregion: str
    iso2: str
    iso3: str
    wikidata_id: str


@strawberry_django.type(State, filters=StateFilter, order=StateOrder, pagination=True)
class StateQuery:
    id: auto
    name: auto
    geometry: str
    adm1_code: str
    iso_3166_1_2: str
    fips: str
    state_type: str
    country: str


@strawberry_django.type(City, filters=CityFilter, order=CityOrder, pagination=True)
class CityQuery:
    id: auto
    name: auto
    point: str
    city_type: str
    country: str
    wikidata_id: str
    whosonfirst_id: str
    geonames_id: str
