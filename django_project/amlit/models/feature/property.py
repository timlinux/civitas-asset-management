__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '09/09/20'

from django.contrib.gis.db import models
from amlit.models.feature import (
    FeatureLine, FeaturePoint, FeaturePolygon
)


class Property(models.Model):
    """
    This is additional property for the feature
    """
    name = models.CharField(max_length=512)
    value = models.CharField(max_length=512)

    class Meta:
        ordering = ('name',)
        abstract = True

    def __str__(self):
        return self.name


class FeaturePointProperty(Property):
    feature = models.ForeignKey(
        FeaturePoint, on_delete=models.CASCADE)

    class Meta:
        db_table = 'feature_point_property'


class FeatureLineProperty(Property):
    feature = models.ForeignKey(
        FeatureLine, on_delete=models.CASCADE)

    class Meta:
        db_table = 'feature_line_property'


class FeaturePolygonProperty(Property):
    feature = models.ForeignKey(
        FeaturePolygon, on_delete=models.CASCADE)

    class Meta:
        db_table = 'feature_polygon_property'
