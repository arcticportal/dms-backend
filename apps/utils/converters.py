from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon


def pandas_to_gis_multipoint(geometry):
    try:
        geometry = GEOSGeometry(str(geometry))
    except (TypeError, ValueError):
        return None
    if geometry.geom_type == "Point":
        return MultiPoint(geometry)
    elif geometry.geom_type == "MultiPoint":
        return geometry
    return None


def pandas_to_gis_multipolygon(geometry):
    try:
        geometry = GEOSGeometry(str(geometry))
    except (TypeError, ValueError):
        return None
    if geometry.geom_type == "Polygon":
        return MultiPolygon(geometry)
    elif geometry.geom_type == "MultiPolygon":
        return geometry
    return None
