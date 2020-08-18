__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base import _Term
from amlit.models.water_supply.general import WaterGeneralBrand
from amlit.models.water_supply.base import WaterSupplyFeature


class MeterType(_Term):
    """ List of Meter Type."""

    class Meta:
        db_table = 'meter_type'


class MeterReadingType(_Term):
    """ List of Meter Reading Type."""

    class Meta:
        db_table = 'meter_reading_type'


class MeterPID(_Term):
    """ List of Meter PID."""

    class Meta:
        db_table = 'meter_pid'


class Meter(WaterSupplyFeature):
    """
    WaterSupply (PWS) sub-feature : Meter
    """
    geometry = models.PointField(
        help_text="Geometry of Meter."
    )
    brand = models.ForeignKey(
        WaterGeneralBrand,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    model = models.CharField(
        max_length=256,
        null=True, blank=True,
        help_text='Model of Meter'
    )
    type = models.ForeignKey(
        MeterType,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    reading_type = models.ForeignKey(
        MeterReadingType,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    pid = models.ForeignKey(
        MeterPID,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        db_table = 'meter'
