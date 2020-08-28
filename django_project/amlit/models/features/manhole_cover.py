__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base_feature import BaseFeature
from amlit.models.features.manhole_trunk import ManholeTrunk


class ManholeCover(BaseFeature):
    """
    sub-class : ManholeCover
    """
    geometry = models.PointField(
        help_text="Geometry of ManholeCover."
    )
    trunk = models.OneToOneField(
        ManholeTrunk, on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'manhole_cover'
