__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base import _Term
from amlit.models.water_supply.general import WaterGeneralBrand
from amlit.models.water_supply.base import WaterSupplyFeature
from amlit.models.water_supply.motor import Motor


class PumpType(_Term):
    """ List of pump type."""

    class Meta:
        db_table = 'pump_type'


class PumpSubType(_Term):
    """ List of pump sub type."""
    type = models.ForeignKey(
        PumpType,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'pump_sub_type'


class Pump(WaterSupplyFeature):
    """
    WaterSupply (PWS) sub-feature : Pump
    """
    geometry = models.PointField(
        help_text="Geometry of pump."
    )
    motor = models.ForeignKey(
        Motor,
        on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        WaterGeneralBrand,
        on_delete=models.CASCADE
    )
    model = models.CharField(
        max_length=256,
        help_text='Model of pump'
    )
    subtype = models.ForeignKey(
        PumpSubType,
        on_delete=models.CASCADE
    )
    submerged = models.BooleanField(
        null=True, blank=True,
        help_text='Pump is submerged'
    )
    capacity = models.FloatField(
        null=True, blank=True,
        help_text='Capacity of pump (SI system)'
    )
    head = models.FloatField(
        null=True, blank=True,
        help_text='Head of pump (SI system)'
    )

    class Meta:
        db_table = 'pump'
