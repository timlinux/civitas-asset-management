__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base import _Term
from amlit.models.water_supply.general import WaterGeneralBrand
from amlit.models.water_supply.base import WaterSupplyFeature


class HydrantType(_Term):
    """ List of Hydrant type."""

    class Meta:
        db_table = 'Hydrant_type'


class Hydrant(WaterSupplyFeature):
    """
    WaterSupply (PWS) sub-feature : Hydrant
    """
    geometry = models.PointField(
        help_text="Geometry of tank."
    )
    brand = models.ForeignKey(
        WaterGeneralBrand,
        on_delete=models.CASCADE
    )
    model = models.CharField(
        max_length=256,
        help_text='Model of hydrant'
    )
    type = models.ForeignKey(
        HydrantType,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'Hydrant'
