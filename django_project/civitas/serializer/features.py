__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/11/20'
from rest_framework import serializers
from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer, GeometrySerializerMethodField)

from civitas.models.feature.feature_geometry import FeatureGeometry
from civitas.models.view.feature_calculations import FeatureCalculation


class FeatureCalculationGeoSerializer(GeoFeatureModelSerializer):
    id = serializers.SerializerMethodField()
    geometry = GeometrySerializerMethodField()
    cls = serializers.SerializerMethodField()
    sub_cls = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    quantity = serializers.SerializerMethodField()
    renewal = serializers.SerializerMethodField()
    maintenance = serializers.SerializerMethodField()
    annual_reserve = serializers.SerializerMethodField()

    def get_id(self, obj):
        """
        :type obj: FeatureCalculation
        """
        return obj.feature.id

    def get_geometry(self, obj):
        """ Get geometry
        :type obj: FeatureCalculation
        """
        try:
            return obj.feature.featuregeometry.geometry()
        except FeatureGeometry.DoesNotExist:
            return None

    def get_cls(self, obj):
        """
        :type obj: FeatureCalculation
        """
        try:
            return obj.feature.the_class.id
        except AttributeError:
            return None

    def get_sub_cls(self, obj):
        """
        :type obj: FeatureCalculation
        """
        return obj.feature.sub_class.id

    def get_type(self, obj):
        """
        :type obj: FeatureCalculation
        """
        return obj.feature.type.id

    def get_quantity(self, obj):
        """
        :type obj: FeatureCalculation
        """
        return obj.feature.quantity if obj.feature.quantity else 0

    def get_renewal(self, obj):
        """
        :type obj: FeatureCalculation
        """
        return obj.renewal_cost()

    def get_maintenance(self, obj):
        """
        :type obj: FeatureCalculation
        """
        return obj.maintenance_cost()

    def get_annual_reserve(self, obj):
        """
        :type obj: FeatureCalculation
        """
        return obj.annual_reserve_cost()

    class Meta:
        model = FeatureCalculation
        geo_field = 'geometry'
        exclude = [
            'estimated_renewal_cost', 'estimated_annual_maintenance_cost', 'estimated_annual_reserve',
            'lifespan', 'age',
            'remaining_years_age_based', 'remaining_percent_age_based', 'remaining_years_condition_based',
            'remaining_percent_condition_based'
        ]


class FeatureGeometryGeoSerializer(GeoFeatureModelSerializer):
    geometry = GeometrySerializerMethodField()

    def get_geometry(self, obj):
        """ Get geometry
        :type obj: FeatureGeometry
        """
        try:
            return obj.geometry()
        except FeatureGeometry.DoesNotExist:
            return None

    class Meta:
        model = FeatureGeometry
        geo_field = 'geometry'
        fields = ('id',)
