# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import os
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get

from django.db import migrations


def import_data(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    app_name = 'aim'
    DJANGO_ROOT = os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        ))

    fixture_file = os.path.join(
        DJANGO_ROOT, 'aim', 'fixtures', 'feature_class.xlsx')
    sheet = xlsx_get(fixture_file, column_limit=11)
    sheetname = next(iter(sheet))
    records = sheet[sheetname]

    # create asset class
    AssetClass = apps.get_model(app_name, 'AssetClass')
    for record in records[1:]:
        name = record[0]
        if name:
            description = record[1]
            print('{} - {}'.format(name, description))
            AssetClass.objects.using(db_alias).get_or_create(
                name=name,
                defaults={'description': description}
            )

    # create asset sub class
    AssetSubClass = apps.get_model(app_name, 'AssetSubClass')
    for record in records[1:]:
        name = record[3]
        if name:
            description = record[4]
            asset_class = record[5]
            print('{} - {} - {}'.format(name, description, asset_class))
            try:
                asset_class = AssetClass.objects.using(db_alias).get(
                    name=asset_class
                )
                sub_class, created = AssetSubClass.objects.using(
                    db_alias).get_or_create(
                    name=name,
                    defaults={
                        'description': description
                    }
                )
                asset_class.sub_classes.add(sub_class)
            except AssetClass.DoesNotExist:
                pass

    # create feature code
    FeatureCode = apps.get_model(app_name, 'FeatureCode')
    for record in records[1:]:
        name = record[7]
        if name:
            description = record[8]
            asset_class = record[9]
            asset_sub_class = record[10]
            print('{} - {} - {} - {}'.format(
                name, description, asset_class, asset_sub_class))
            try:
                asset_class = AssetClass.objects.using(db_alias).get(
                    name=asset_class
                )
                asset_sub_class = AssetSubClass.objects.using(db_alias).get(
                    name=asset_sub_class
                )
                FeatureCode.objects.using(
                    db_alias).get_or_create(
                    name=name,
                    defaults={
                        'description': description,
                        'asset_class': asset_class,
                        'asset_sub_class': asset_sub_class
                    }
                )
            except (AssetClass.DoesNotExist, AssetSubClass.DoesNotExist):
                pass


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('aim', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_data),
    ]
