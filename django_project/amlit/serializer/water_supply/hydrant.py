__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from amlit.models.water_supply import Hydrant
from amlit.serializer.base import FeatureBaseSerializer


class HydrantGeoSerializer(FeatureBaseSerializer):
    material = None

    class Meta:
        model = Hydrant
        geo_field = 'geometry'
        exclude = []
