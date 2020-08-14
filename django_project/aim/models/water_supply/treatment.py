__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from aim.models.base import _Term
from aim.models.water_supply.base import WaterSupplyFeature


class TreatmentType(_Term):
    """ List of treatment type."""

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
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'treatment'
