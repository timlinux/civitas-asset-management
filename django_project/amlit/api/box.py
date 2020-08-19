__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from amlit.api.base import SingleObjectAPI
from amlit.models.water_supply import Box
from amlit.serializer.water_supply import BoxGeoSerializer


class GetBoxGeojson(SingleObjectAPI):
    """
    get:
    Return geojson of boundaries.
    """
    Model = Box
    Serializer = BoxGeoSerializer
