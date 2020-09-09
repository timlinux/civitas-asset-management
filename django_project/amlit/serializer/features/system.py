__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from rest_framework import serializers
from rest_framework_gis.serializers import ModelSerializer
from amlit.models.system import System
from amlit.serializer.community import CommunitySerializer


class SystemSerializer(ModelSerializer):
    features = serializers.SerializerMethodField()
    community = serializers.SerializerMethodField()

    def get_features(self, obj):
        """ Return boxes data in geojson """
        return {
            # 'boxes': BoxGeoSerializer(obj.boxes, many=True).data,
            # 'chambers': ChamberGeoSerializer(obj.chambers, many=True).data,
            # 'hydrants': HydrantGeoSerializer(obj.hydrants, many=True).data,
            # 'meters': MeterGeoSerializer(obj.meters, many=True).data,
            # 'pipes': PipeGeoSerializer(obj.pipes, many=True).data,
        }

    def get_community(self, obj):
        """ Return community """
        return CommunitySerializer(obj.community).data

    class Meta:
        model = System
        fields = ['id', 'features', 'community', 'name', 'description']
