__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base_feature import BaseFeature


class ManholeTrunk(BaseFeature):
    """
    sub-class : ManholeTrunk
    """
    geometry = models.PointField(
        help_text="Geometry of ManholeTrunk."
    )

    class Meta:
        db_table = 'manhole_trunk'
