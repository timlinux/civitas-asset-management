__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base_feature import BaseFeature


class Source(BaseFeature):
    """
    sub-class : Source
    """
    geometry = models.PolygonField(
        help_text="Geometry of source."
    )

    class Meta:
        db_table = 'source'
