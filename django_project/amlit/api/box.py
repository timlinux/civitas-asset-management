__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from amlit.api.base import SingleObjectAPI
from amlit.models.features import Box
from amlit.serializer.features import BoxGeoSerializer


class GetBoxGeojson(SingleObjectAPI):
    """
    get:
    Return geojson of boundaries.
    """
    Model = Box
    Serializer = BoxGeoSerializer
