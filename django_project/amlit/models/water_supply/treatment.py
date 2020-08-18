__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base import _Term
from amlit.models.water_supply.base import WaterSupplyFeature


class TreatmentType(_Term):
    """ List of Treatment Type."""

    class Meta:
        db_table = 'treatment_type'


class Treatment(WaterSupplyFeature):
    """
    WaterSupply (PWS) sub-feature : Treatment
    """
    geometry = models.PolygonField(
        help_text="Geometry of tank."
    )
    type = models.ForeignKey(
        TreatmentType,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        db_table = 'treatment'
