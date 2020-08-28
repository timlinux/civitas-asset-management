__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base_feature import BaseFeature
from amlit.models.features.general import (
    GeneralBrand, GeneralMaterial)


class Pipe(BaseFeature):
    """
    sub-class : Pipe
    """
    geometry = models.LineStringField(
        help_text="Geometry of Pipe."
    )
    brand = models.ForeignKey(
        GeneralBrand,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    model = models.CharField(
        max_length=256,
        null=True, blank=True,
        help_text='Model of Pipe'
    )
    material = models.ForeignKey(
        GeneralMaterial,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    diameter = models.FloatField(
        null=True, blank=True,
        help_text='Depth of pipe (SI system)'
    )
    depth = models.FloatField(
        null=True, blank=True,
        help_text='Depth of pipe (SI system)'
    )
    length = models.FloatField(
        null=True, blank=True,
        help_text='Length of pipe (SI system)'
    )

    class Meta:
        db_table = 'pipe'
