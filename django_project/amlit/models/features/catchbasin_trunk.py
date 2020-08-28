__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base_feature import BaseFeature


class CatchbasinTrunk(BaseFeature):
    """
    sub-class : CatchbasinTrunk
    """
    geometry = models.PointField(
        help_text="Geometry of CatchbasinGrate."
    )

    class Meta:
        db_table = 'catchbasin_trunk'
