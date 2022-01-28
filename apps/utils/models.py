from django.contrib.gis.db import models


class Thing(models.Model):
    name = models.CharField(max_length=1024, null=True, blank=True)
    name_long = models.CharField(max_length=2048, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    wikipedia_url = models.URLField(null=True, blank=True)
    wikidata_id = models.CharField(max_length=16, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Place(Thing):
    geometry = models.MultiPolygonField(null=True, blank=True)
    point = models.MultiPointField(null=True, blank=True)

    class Meta:
        abstract = True
