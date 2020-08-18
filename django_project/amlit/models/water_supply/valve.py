__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.base import _Term
from amlit.models.water_supply.general import WaterGeneralBrand
from amlit.models.water_supply.base import WaterSupplyFeature


class ValveType(_Term):
    """ List of Valve type."""

    class Meta:
        db_table = 'valve_type'


class ValveActuationType(_Term):
    """ List of Valve actuation type."""

    class Meta:
        db_table = 'valve_actuation_type'


class ValveActuationDirection(_Term):
    """ List of Valve actuation direction."""

    class Meta:
        db_table = 'valve_actuation_direction'


class ValveActuationSpec(_Term):
    """ List of Valve actuation spec."""

    class Meta:
        db_table = 'valve_actuation_spec'


class Valve(WaterSupplyFeature):
    """
    WaterSupply (PWS) sub-feature : Valve
    """
    geometry = models.PolygonField(
        help_text="Geometry of Valve."
    )
    brand = models.ForeignKey(
        WaterGeneralBrand,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    model = models.CharField(
        max_length=256,
        null=True, blank=True,
        help_text='Model of Valve'
    )
    type = models.ForeignKey(
        ValveType,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    diameter = models.FloatField(
        null=True, blank=True,
        help_text='Diameter of valve (SI system)'
    )
    actuation_type = models.ForeignKey(
        ValveActuationType,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    actuation_direction = models.ForeignKey(
        ValveActuationDirection,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    actuation_spec = models.ForeignKey(
        ValveActuationSpec,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    depth = models.FloatField(
        null=True, blank=True,
        help_text='Depth of valve (SI system)'
    )

    class Meta:
        db_table = 'valve'
