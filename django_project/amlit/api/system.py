__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from amlit.api.base import (
    SingleObjectAPI, MultiObjectAPI)
from amlit.models.system import System
from amlit.serializer.features.system import (
    SystemSerializer
)


class GetSystem(SingleObjectAPI):
    """
    get:
    Return system of features
    """
    Model = System
    Serializer = SystemSerializer


class GetSystems(MultiObjectAPI):
    """
    get:
    Return system of features
    """
    Model = System
    Serializer = SystemSerializer
