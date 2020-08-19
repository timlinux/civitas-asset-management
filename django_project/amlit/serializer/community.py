__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from rest_framework import serializers
from rest_framework_gis.serializers import ModelSerializer
from amlit.models.community import Community


class CommunitySerializer(ModelSerializer):
    province = serializers.SerializerMethodField()
    region = serializers.SerializerMethodField()
    community = serializers.SerializerMethodField()

    def get_province(self, obj):
        """ Return province of province """
        return obj.region.province.__str__()

    def get_region(self, obj):
        """ Return province of region """
        return obj.region.__str__()

    def get_community(self, obj):
        """ Return province of community """
        return obj.__str__()

    class Meta:
        model = Community
        fields = ['community', 'region', 'province']
