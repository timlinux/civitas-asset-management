__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base import _Term
from amlit.models.water_supply.base import WaterSupplyFeature


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
        null=True, blank=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        db_table = 'source'
