__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base_feature import BaseFeature


class Retention(BaseFeature):
    """
    sub-class : Retention
    """
    geometry = models.GeometryField(
        help_text="Geometry of Retention."
    )

    class Meta:
        db_table = 'retention'
