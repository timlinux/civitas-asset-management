__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from amlit.api.base import (
    SingleObjectAPI, MultiObjectAPI)
from amlit.models.water_supply import WaterSystem
from amlit.serializer.water_supply.water_system import (
    WaterSystemSerializer
)


class GetWaterSystem(SingleObjectAPI):
    """
    get:
    Return water system data
    """
    Model = WaterSystem
    Serializer = WaterSystemSerializer


class GetWaterSystems(MultiObjectAPI):
    """
    get:
    Return water system data
    """
    Model = WaterSystem
    Serializer = WaterSystemSerializer
