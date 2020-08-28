__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base_feature import BaseFeature
from amlit.models.features.catchbasin_trunk import CatchbasinTrunk


class CatchbasinGrate(BaseFeature):
    """
    sub-class : CatchbasinGrate
    """
    geometry = models.PointField(
        help_text="Geometry of CatchbasinGrate."
    )

    trunk = models.OneToOneField(
        CatchbasinTrunk, on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'catchbasin_grate'
