__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.water_supply.general import (
    WaterGeneralBrand, WaterGeneralMaterial)
from amlit.models.water_supply.base import WaterSupplyFeature


class Control(WaterSupplyFeature):
    """
    WaterSupply (PWS) sub-feature : Control
    """

    class Meta:
        db_table = 'control'
