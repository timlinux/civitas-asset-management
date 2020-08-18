__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base import _Term
from amlit.models.water_supply.general import (
    WaterGeneralBrand, WaterGeneralMaterial)
from amlit.models.water_supply.base import WaterSupplyFeature


class PartType(_Term):
    """ List of Part type."""

    class Meta:
        db_table = 'part_type'


class Part(WaterSupplyFeature):
    """
    WaterSupply (PWS) sub-feature : Part
    """
    geometry = models.PolygonField(
        help_text="Geometry of Part."
    )
    brand = models.ForeignKey(
        WaterGeneralBrand,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    model = models.CharField(
        max_length=256,
        null=True, blank=True,
        help_text='Model of Part'
    )
    type = models.ForeignKey(
        PartType,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    material = models.ForeignKey(
        WaterGeneralMaterial,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    depth = models.FloatField(
        null=True, blank=True,
        help_text='Depth of part (SI system)'
    )

    class Meta:
        db_table = 'part'
