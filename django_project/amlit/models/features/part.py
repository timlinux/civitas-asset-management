__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base_feature import BaseFeature
from amlit.models.features.general import (
    GeneralBrand, GeneralMaterial)


class Part(BaseFeature):
    """
    sub-class : Part
    """
    geometry = models.PointField(
        help_text="Geometry of Part."
    )
    brand = models.ForeignKey(
        GeneralBrand,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    model = models.CharField(
        max_length=256,
        null=True, blank=True,
        help_text='Model of Part'
    )
    material = models.ForeignKey(
        GeneralMaterial,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    depth = models.FloatField(
        null=True, blank=True,
        help_text='Depth of part (SI system)'
    )

    class Meta:
        db_table = 'part'
