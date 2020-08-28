__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from amlit.models.features import Pipe
from amlit.serializer.base import FeatureBaseSerializer


class PipeGeoSerializer(FeatureBaseSerializer):
    class Meta:
        model = Pipe
        geo_field = 'geometry'
        exclude = []
