__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.abstract import _Term
from amlit.models.base_feature import BaseFeature
from amlit.models.features.general import GeneralBrand


class MeterReadingType(_Term):
    """ List of Meter Reading Type."""

    class Meta:
        db_table = 'meter_reading_type'


class MeterPID(_Term):
    """ List of Meter PID."""

    class Meta:
        db_table = 'meter_pid'


class Meter(BaseFeature):
    """
    sub-class : Meter
    """
    geometry = models.PointField(
        help_text="Geometry of Meter."
    )
    brand = models.ForeignKey(
        GeneralBrand,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    model = models.CharField(
        max_length=256,
        null=True, blank=True,
        help_text='Model of Meter'
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
