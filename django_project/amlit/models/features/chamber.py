__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.features.general import GeneralBrand
from amlit.models.base_feature import BaseFeature


class Chamber(BaseFeature):
    """
    sub-class : Chamber
    """
    geometry = models.PointField(
        help_text="Geometry of Chamber."
    )
    brand = models.ForeignKey(
        GeneralBrand,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    model = models.CharField(
        max_length=256,
        null=True, blank=True,
        help_text='Model of Chamber'
    )

    class Meta:
        db_table = 'chamber'
