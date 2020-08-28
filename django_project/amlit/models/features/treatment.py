__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base_feature import BaseFeature


class Treatment(BaseFeature):
    """
    sub-class : Treatment
    """
    geometry = models.PolygonField(
        help_text="Geometry of tank."
    )

    class Meta:
        db_table = 'treatment'
