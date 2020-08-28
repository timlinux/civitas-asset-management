__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base_feature import BaseFeature
from amlit.models.features.general import GeneralBrand
from amlit.models.features.motor import Motor


class Pump(BaseFeature):
    """
    sub-class : Pump
    """
    geometry = models.PointField(
        help_text="Geometry of pump."
    )
    motor = models.ForeignKey(
        Motor,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    brand = models.ForeignKey(
        GeneralBrand,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    model = models.CharField(
        max_length=256,
        null=True, blank=True,
        help_text='Model of pump'
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
