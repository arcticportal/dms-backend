# Generated by Django 3.2.11 on 2022-01-28 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrative_area', '0002_auto_20220128_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
            ],
            options={
                'verbose_name': 'State Type',
                'verbose_name_plural': 'State types',
                'db_table': 'state_type',
            },
        ),
        migrations.AddField(
            model_name='state',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrative_area.country'),
        ),
        migrations.AddField(
            model_name='state',
            name='fips',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='state_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrative_area.statetype'),
        ),
    ]