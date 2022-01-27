# Generated by Django 3.2.11 on 2022-01-27 14:44

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
                ('name_long', models.CharField(blank=True, max_length=2048, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('wikipedia_url', models.URLField(blank=True, null=True)),
                ('wikidata_id', models.CharField(blank=True, max_length=16, null=True)),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('point', django.contrib.gis.db.models.fields.MultiPointField(blank=True, null=True, srid=4326)),
            ],
            options={
                'verbose_name': 'Continent',
                'verbose_name_plural': 'Continents',
                'db_table': 'continent',
            },
        ),
        migrations.CreateModel(
            name='OceanBodyOfWater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
                ('name_long', models.CharField(blank=True, max_length=2048, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('wikipedia_url', models.URLField(blank=True, null=True)),
                ('wikidata_id', models.CharField(blank=True, max_length=16, null=True)),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('point', django.contrib.gis.db.models.fields.MultiPointField(blank=True, null=True, srid=4326)),
            ],
            options={
                'verbose_name': 'Ocean',
                'verbose_name_plural': 'Oceans',
                'db_table': 'ocean_body_of_water',
            },
        ),
    ]
