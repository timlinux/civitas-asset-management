__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from aim.models.base import _Term
from aim.models.water_supply.base import WaterSupplyFeature


class SourceType(_Term):
    """ List of source type."""

    class Meta:
        db_table = 'source_type'


class Source(WaterSupplyFeature):
    """
    WaterSupply (PWS) sub-feature : Source
    """
    geometry = models.PolygonField(
        help_text="Geometry of source."
    )
    type = models.ForeignKey(
        SourceType,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'source'
