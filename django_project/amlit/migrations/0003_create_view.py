# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('amlit', '0002_initial_feature_class'),
    ]
    point_view = """
    CREATE VIEW feature_point_view AS 
    SELECT point.*, class.name as class, sub.name as sub_class, type.name as type
    from feature_point as point
           LEFT JOIN asset_type_combination comb on point.type_id = comb.id
           LEFT JOIN asset_class class on comb.class = class.id
           LEFT JOIN asset_sub_class sub on comb.sub_class_id = sub.id
           LEFT JOIN asset_type type on comb.type_id = type.id;
    """

    line_view = """
        CREATE VIEW feature_line_view AS 
    SELECT line.*, class.name as class, sub.name as sub_class, type.name as type
    from feature_line as line
           LEFT JOIN asset_type_combination comb on line.type_id = comb.id
           LEFT JOIN asset_class class on comb.class = class.id
           LEFT JOIN asset_sub_class sub on comb.sub_class_id = sub.id
           LEFT JOIN asset_type type on comb.type_id = type.id;
        """

    polygon_view = """
        CREATE VIEW feature_polygon_view AS 
    SELECT polygon.*, class.name as class, sub.name as sub_class, type.name as type
    from feature_polygon as polygon
           LEFT JOIN asset_type_combination comb on polygon.type_id = comb.id
           LEFT JOIN asset_class class on comb.class = class.id
           LEFT JOIN asset_sub_class sub on comb.sub_class_id = sub.id
           LEFT JOIN asset_type type on comb.type_id = type.id;
        """

    operations = [
        migrations.RunSQL('DROP VIEW IF EXISTS features_view;'),
        migrations.RunSQL(point_view),
        migrations.RunSQL(line_view),
        migrations.RunSQL(polygon_view)
    ]
