__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from amlit.models.water_supply import Chamber
from amlit.serializer.base import FeatureBaseSerializer


class ChamberGeoSerializer(FeatureBaseSerializer):
    material = None

    class Meta:
        model = Chamber
        geo_field = 'geometry'
        exclude = []
