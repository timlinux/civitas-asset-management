__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from amlit.models.abstract import _Term
from amlit.models.base_feature import BaseFeature
from amlit.models.features import Box
from amlit.models.features.general import GeneralBrand


class ValveActuationType(_Term):
    """ List of Valve Actuation Type."""

    class Meta:
        db_table = 'valve_actuation_type'


class ValveActuationDirection(_Term):
    """ List of Valve Actuation Direction."""

    class Meta:
        db_table = 'valve_actuation_direction'


class ValveActuationSpec(_Term):
    """ List of Valve Actuation Spec."""

    class Meta:
        db_table = 'valve_actuation_spec'


class Valve(BaseFeature):
    """
    sub-class : Valve
    """
    geometry = models.PointField(
        help_text="Geometry of Valve."
    )
    box = models.ForeignKey(
        Box,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    brand = models.ForeignKey(
        GeneralBrand,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    model = models.CharField(
        max_length=256,
        null=True, blank=True,
        help_text='Model of Valve'
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
