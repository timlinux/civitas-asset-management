__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base_feature import BaseFeature
from amlit.models.features import Control


class Motor(BaseFeature):
    """
    sub-class : Motor
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
