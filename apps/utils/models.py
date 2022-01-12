from django.contrib.gis.db import models


class Thing(models.Model):
    name = models.CharField(max_length=1024, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    class Meta:
        db_tables = "things"

    def __str__(self):
        return self.name


class Place(Thing):
    geo = models.MultiPolygonField(null=True, blank=True)
