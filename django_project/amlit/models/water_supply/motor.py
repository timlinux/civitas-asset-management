__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base import _Term
from amlit.models.water_supply import Control
from amlit.models.water_supply.base import WaterSupplyFeature


class MotorType(_Term):
    """ List of Motor Type."""

    class Meta:
        db_table = 'motor_type'


class Motor(WaterSupplyFeature):
    """
    WaterSupply (PWS) sub-feature : Motor
    """
    geometry = models.PointField(
        help_text="Geometry of motor."
    )
    control = models.ForeignKey(
        Control,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    model = models.CharField(
        max_length=256,
        null=True, blank=True,
        help_text='Model of motor'
    )
    type = models.ForeignKey(
        MotorType,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    output_hp = models.FloatField(
        null=True, blank=True,
        help_text='Output HP of motor (SI system)'
    )
    output_power = models.FloatField(
        null=True, blank=True,
        help_text='Output HP of motor (SI system)'
    )

    class Meta:
        db_table = 'motor'
