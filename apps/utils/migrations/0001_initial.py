# Generated by Django 3.2.11 on 2022-01-13 09:26

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
                ('name_long', models.CharField(blank=True, max_length=2048, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('thing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='utils.thing')),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
            ],
            bases=('utils.thing',),
        ),
    ]