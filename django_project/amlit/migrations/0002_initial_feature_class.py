# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import os
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get

from django.db import migrations


def get_term_from_records(sheet, sheet_name):
    """ Return term records as dictionary
    The pattern needs:
    1. title is second row
    2. column is empty, id, name, description

    :param sheet: the sheet that already opened
    :param sheet_name:
    :type sheet_name: str
    :return: dict
    """
    records = sheet[sheet_name]
    data = {}
    for record in records[2:]:
        # check if id exist
        try:
            id = record[1]
            if not id:
                break
        except IndexError:
            continue

        name = record[2]
        description = record[3]
        data[id] = {
            'name': name,
            'description': description.capitalize(),
            'obj': None
        }
        try:
            data[id]['foreign_key'] = record[4]
        except IndexError:
            pass
    return data


def get_type_value_from_records(sheet, sheet_name):
    """ Return value records of typs as dictionary
    The pattern needs:
    1. title is second row
    2. column is empty, empty, value, type_id

    :param sheet: the sheet that already opened
    :param sheet_name:
    :type sheet_name: str
    :return: dict
    """
    records = sheet[sheet_name]
    data = {}
    for record in records[2:]:
        # check if id exist
        try:
            type = record[3]
            if not type:
                break
        except IndexError:
            continue

        data[type] = record[2]
    return data


def import_data(apps, schema_editor):
    # EXTRACT DATA
    filename = 'CAM value list.xlsx'
    DJANGO_ROOT = os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        ))

    fixture_file = os.path.join(
        DJANGO_ROOT, 'amlit', 'fixtures', filename)
    sheet = xlsx_get(fixture_file, column_limit=11)
    classes = get_term_from_records(sheet, 'class')
    subclasses = get_term_from_records(sheet, 'subclass')
    types = get_term_from_records(sheet, 'type')
    units = get_term_from_records(sheet, 'unit_valuelist')
    type_unit = get_type_value_from_records(sheet, 'unit_lookup')
    type_life = get_type_value_from_records(
        sheet, 'life_lookup')
    type_renewal_cost = get_type_value_from_records(
        sheet, 'renewal_cost_lookup')
    type_maintenance_cost = get_type_value_from_records(
        sheet, 'maintenance_cost_lookup')

    # INSERT INTO DATABASE
    # To prevent the indexing error (insert id directly)
    # we need to check the data from their id in data
    # and put obj in the data

    db_alias = schema_editor.connection.alias
    app_name = 'amlit'

    # units
    Unit = apps.get_model(app_name, 'Unit')
    for key, data in units.items():
        obj, created = Unit.objects.using(db_alias).get_or_create(
            name=data['name'],
            defaults={'description': data['description']}
        )
        data['obj'] = obj

    # class
    FeatureClass = apps.get_model(app_name, 'FeatureClass')
    for key, data in classes.items():
        obj, created = FeatureClass.objects.using(db_alias).get_or_create(
            name=data['name'],
            defaults={'description': data['description']}
        )
        data['obj'] = obj

    # sub class
    FeatureSubClass = apps.get_model(app_name, 'FeatureSubClass')
    for key, data in subclasses.items():
        foreign_key = classes[data['foreign_key']]['obj']
        obj, created = FeatureSubClass.objects.using(db_alias).get_or_create(
            name=data['name'],
            the_class=foreign_key,
            defaults={'description': data['description']}
        )
        data['obj'] = obj

    Currency = apps.get_model(app_name, 'Currency')
    Money = apps.get_model(app_name, 'Money')
    canadian, created = Currency.objects.using(db_alias).get_or_create(
        code='$',
        name='Canadian Dollar'
    )
    # types
    FeatureType = apps.get_model(app_name, 'FeatureType')
    for key, data in types.items():
        foreign_key = subclasses[data['foreign_key']]['obj']
        obj, created = FeatureType.objects.using(db_alias).get_or_create(
            name=data['name'],
            sub_class=foreign_key
        )

        renewal_cost = type_renewal_cost[key] if key in type_renewal_cost else None
        if renewal_cost and not obj.renewal_cost:
            obj.renewal_cost = Money.objects.using(db_alias).create(
                currency=canadian,
                value=renewal_cost
            )

        maintenance_cost = type_maintenance_cost[key] if key in type_maintenance_cost else None
        if maintenance_cost and not obj.maintenance_cost:
            obj.maintenance_cost = Money.objects.using(db_alias).create(
                currency=canadian,
                value=maintenance_cost
            )

        obj.description = data['description']
        obj.unit = units[type_unit[key]]['obj'] if key in type_unit else None
        obj.lifespan = type_life[key] if key in type_life else None
        obj.save()

        data['obj'] = obj

    raise Exception('')


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('amlit', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_data),
    ]
