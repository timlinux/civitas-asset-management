__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class FeatureBaseSerializer(GeoFeatureModelSerializer):
    asset_class = serializers.SerializerMethodField()
    asset_sub_class = serializers.SerializerMethodField()
    feature_code = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    material = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    def get_feature_code(self, obj):
        """ Return feature code string """
        return obj.feature_code.__str__()

    def get_asset_class(self, obj):
        """ Return asset class string from feature code """
        return obj.feature_code.asset_class.__str__()

    def get_asset_sub_class(self, obj):
        """ Return asset sub class string from feature code """
        return obj.feature_code.asset_sub_class.__str__()

    def get_brand(self, obj):
        """ Return brand string """
        return obj.brand.__str__()

    def get_material(self, obj):
        """ Return material string """
        return obj.material.__str__()

    def get_type(self, obj):
        """ Return material string """
        return obj.type.__str__()

    class Meta:
        abstract = True
        geo_field = 'geometry'
        exclude = []
