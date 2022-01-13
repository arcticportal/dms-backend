import strawberry_django
from apps.administrative_area.models import Country as CountryModel

@strawberry_django.type(CountryModel)
class Country:
    fips_10: str
    continent: str
    