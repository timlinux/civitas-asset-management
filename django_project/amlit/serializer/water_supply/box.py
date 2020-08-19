__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from amlit.models.water_supply import Box
from amlit.serializer.base import FeatureBaseSerializer


class BoxGeoSerializer(FeatureBaseSerializer):
    type = None

    class Meta:
        model = Box
        geo_field = 'geometry'
        exclude = []
