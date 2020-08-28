__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base_feature import BaseFeature
from amlit.models.features.general import GeneralBrand


class Hydrant(BaseFeature):
    """
    sub-class : Hydrant
    """
    geometry = models.PointField(
        help_text="Geometry of tank."
    )
    brand = models.ForeignKey(
        GeneralBrand,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    model = models.CharField(
        max_length=256,
        help_text='Model of hydrant',
        null=True, blank=True
    )

    class Meta:
        db_table = 'hydrant'
