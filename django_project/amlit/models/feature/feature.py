__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '09/09/20'

from django.contrib.gis.db import models
from amlit.models.feature.base_feature import BaseFeature


class FeaturePoint(BaseFeature):
    geometry = models.MultiPointField(
        help_text="Multipoint Geometry."
    )

    class Meta:
        db_table = 'feature_point'


class FeatureLine(BaseFeature):
    geometry = models.MultiLineStringField(
        help_text="Multiline Geometry."
    )

    class Meta:
        db_table = 'feature_line'


class FeaturePolygon(BaseFeature):
    geometry = models.MultiPolygonField(
        help_text="Multipolygon Geometry."
    )

    class Meta:
        db_table = 'feature_polygon'
