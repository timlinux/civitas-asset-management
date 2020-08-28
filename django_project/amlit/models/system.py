__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/08/20'

from django.contrib.gis.db import models
from amlit.models.abstract import _Term
from amlit.models.community import Community


class System(_Term):
    """
     System is a collection of all of feature
    """
    community = models.ForeignKey(
        Community, blank=True, null=True,
        on_delete=models.SET_NULL
    )

    # TODO:
    #  make sure that use this if feature can be in multiple system
    # boxes = models.ManyToManyField(
    #     Box, blank=True
    # )
    # chambers = models.ManyToManyField(
    #     Chamber, blank=True
    # )
    # controls = models.ManyToManyField(
    #     Control, blank=True
    # )
    # hydrants = models.ManyToManyField(
    #     Hydrant, blank=True
    # )
    # meters = models.ManyToManyField(
    #     Meter, blank=True
    # )
    # motors = models.ManyToManyField(
    #     Motor, blank=True
    # )
    # parts = models.ManyToManyField(
    #     Part, blank=True
    # )
    # pipes = models.ManyToManyField(
    #     Pipe, blank=True
    # )
    # pumps = models.ManyToManyField(
    #     Pump, blank=True
    # )
    # sources = models.ManyToManyField(
    #     Source, blank=True
    # )
    # tanks = models.ManyToManyField(
    #     Tank, blank=True
    # )
    # treatments = models.ManyToManyField(
    #     Treatment, blank=True
    # )
    # valves = models.ManyToManyField(
    #     Valve, blank=True
    # )

    class Meta:
        db_table = 'system'
