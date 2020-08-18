__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base import _Term
from amlit.models.water_supply.general import WaterGeneralBrand
from amlit.models.water_supply.base import WaterSupplyFeature


class ChamberType(_Term):
    """ List of Chamber type."""

    class Meta:
        db_table = 'chamber_type'


class Chamber(WaterSupplyFeature):
    """
    WaterSupply (PWS) sub-feature : Chamber
    """
    geometry = models.PolygonField(
        help_text="Geometry of Chamber."
    )
    brand = models.ForeignKey(
        WaterGeneralBrand,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    model = models.CharField(
        max_length=256,
        null=True, blank=True,
        help_text='Model of Chamber'
    )
    type = models.ForeignKey(
        ChamberType,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        db_table = 'chamber'
