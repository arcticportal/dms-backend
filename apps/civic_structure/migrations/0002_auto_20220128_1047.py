# Generated by Django 3.2.11 on 2022-01-28 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('civic_structure', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airport',
            old_name='mpoly',
            new_name='geometry',
        ),
        migrations.RenameField(
            model_name='boatterminal',
            old_name='mpoly',
            new_name='geometry',
        ),
    ]
