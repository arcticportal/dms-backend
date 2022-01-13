from pathlib import Path

from django.contrib.gis.utils import LayerMapping

from apps.administrative_area.models import Country

world_mapping = {
    "fips_10": "FIPS_10",
    "name": "NAME",
    "name_long": "NAME_LONG",
    "postal": "POSTAL",
    "country_type": "TYPE",
    "wikidata_id": "WIKIDATAID",
    "continent": "CONTINENT",
    "subregion": "SUBREGION",
    "mpoly": "MULTIPOLYGON",
}

world_shp = Path(__file__).resolve().parent / "temp" / "country" / "ne_50m_admin_0_countries.shp"


def run(verbose=True):
    lm = LayerMapping(Country, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
