__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.feature.feature_base import FeatureBase


class FeatureGeometry(models.Model):
    """
    Geometry of feature base
    """

    feature = models.ForeignKey(
        FeatureBase,
        on_delete=models.CASCADE
    )
    geom_point = models.PointField(
        null=True, blank=True
    )
    geom_line = models.LineStringField(
        null=True, blank=True
    )
    geom_polygon = models.PolygonField(
        null=True, blank=True
    )

    class Meta:
        managed = False
        db_table = 'feature_geometry'
