__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/08/20'

from django.contrib.gis.db import models
from amlit.models.base import _Term
from amlit.models.water_supply import (
    Box, Chamber, Control, Hydrant,
    Meter, Motor, Part, Pipe, Pump, Source, Tank, Valve
)
from amlit.models.community import Community


class WaterSystem(_Term):
    """
    WaterSupply System is a collection of all of water supply
    """
    community = models.ForeignKey(
        Community, blank=True, null=True,
        on_delete=models.SET_NULL
    )
    boxes = models.ManyToManyField(
        Box, blank=True
    )
    chamber = models.ManyToManyField(
        Chamber, blank=True
    )
    control = models.ManyToManyField(
        Control, blank=True
    )
    hydrant = models.ManyToManyField(
        Hydrant, blank=True
    )
    meter = models.ManyToManyField(
        Meter, blank=True
    )
    motor = models.ManyToManyField(
        Motor, blank=True
    )
    part = models.ManyToManyField(
        Part, blank=True
    )
    pipe = models.ManyToManyField(
        Pipe, blank=True
    )
    pump = models.ManyToManyField(
        Pump, blank=True
    )
    source = models.ManyToManyField(
        Source, blank=True
    )
    tank = models.ManyToManyField(
        Tank, blank=True
    )
    valve = models.ManyToManyField(
        Valve, blank=True
    )

    class Meta:
        db_table = 'water_system'
