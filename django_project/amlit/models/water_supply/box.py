__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.water_supply.general import (
    WaterGeneralBrand, WaterGeneralMaterial)
from amlit.models.water_supply.base import WaterSupplyFeature


class Box(WaterSupplyFeature):
    """
    WaterSupply (PWS) sub-feature : Box
    """
    geometry = models.PolygonField(
        help_text="Geometry of Box."
    )
    brand = models.ForeignKey(
        WaterGeneralBrand,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    model = models.CharField(
        max_length=256,
        null=True, blank=True,
        help_text='Model of Box'
    )
    material = models.ForeignKey(
        WaterGeneralMaterial,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        db_table = 'box'
