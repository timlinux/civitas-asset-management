__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from rest_framework import serializers
from amlit.models.water_supply import Meter
from amlit.serializer.base import FeatureBaseSerializer


class MeterGeoSerializer(FeatureBaseSerializer):
    material = None
    reading_type = serializers.SerializerMethodField()
    pid = serializers.SerializerMethodField()

    def get_reading_type(self, obj):
        return obj.reading_type.__str__()

    def get_pid(self, obj):
        return obj.pid.__str__()

    class Meta:
        model = Meter
        geo_field = 'geometry'
        exclude = []
