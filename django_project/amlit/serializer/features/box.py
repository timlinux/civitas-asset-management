__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from amlit.models.features import Box
from amlit.serializer.base import FeatureBaseSerializer


class BoxGeoSerializer(FeatureBaseSerializer):
    class Meta:
        model = Box
        geo_field = 'geometry'
        exclude = []
