# Generated by Django 3.2.11 on 2022-02-01 13:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrative_area', '0005_auto_20220201_1155'),
        ('civic_structure', '0002_auto_20220128_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScientificStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
                ('name_long', models.CharField(blank=True, max_length=2048, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('wikipedia_url', models.URLField(blank=True, null=True)),
                ('wikidata_id', models.CharField(blank=True, max_length=16, null=True)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('point', django.contrib.gis.db.models.fields.MultiPointField(blank=True, null=True, srid=4326)),
                ('geonames_id', models.CharField(blank=True, max_length=16, null=True)),
                ('whosonfirst_id', models.CharField(blank=True, max_length=16, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrative_area.country')),
            ],
            options={
                'verbose_name': 'Scientific station',
                'verbose_name_plural': 'Scientific stations',
                'db_table': 'science_station',
            },
        ),
    ]