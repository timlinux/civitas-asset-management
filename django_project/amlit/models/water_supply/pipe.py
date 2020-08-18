__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base import _Term
from amlit.models.water_supply.general import (
    WaterGeneralBrand, WaterGeneralMaterial)
from amlit.models.water_supply.base import WaterSupplyFeature


class PipeType(_Term):
    """ List of Pipe Type."""

    class Meta:
        db_table = 'pipe_type'


class Pipe(WaterSupplyFeature):
    """
    WaterSupply (PWS) sub-feature : Pipe
    """
    geometry = models.LineStringField(
        help_text="Geometry of Pipe."
    )
    brand = models.ForeignKey(
        WaterGeneralBrand,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    model = models.CharField(
        max_length=256,
        null=True, blank=True,
        help_text='Model of Pipe'
    )
    type = models.ForeignKey(
        PipeType,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    material = models.ForeignKey(
        WaterGeneralMaterial,
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
