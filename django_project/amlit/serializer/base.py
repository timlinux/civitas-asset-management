__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class FeatureBaseSerializer(GeoFeatureModelSerializer):
    feature_class = serializers.SerializerMethodField()
    feature_sub_class = serializers.SerializerMethodField()
    feature_code = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    sub_type = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    material = serializers.SerializerMethodField()

    def get_feature_code(self, obj):
        """ Return feature code string """
        return obj.feature_code.__str__()

    def get_type(self, obj):
        """ Return type string """
        return obj.type.__str__()

    def get_sub_type(self, obj):
        """ Return sub type string """
        return obj.sub_type.__str__()

    def get_feature_class(self, obj):
        """ Return feature class string from feature code """
        return obj.type.sub_class.the_class.__str__()

    def get_feature_sub_class(self, obj):
        """ Return feature sub class string from feature code """
        return obj.type.sub_class.__str__()

    def get_brand(self, obj):
        """ Return brand string """
        return obj.brand.__str__()

    def get_material(self, obj):
        """ Return material string """
        return obj.material.__str__()

    class Meta:
        abstract = True
        geo_field = 'geometry'
        exclude = []
