__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from amlit.models.base_feature import (
    AssetClass, AssetSubClass, FeatureCode
)

water_list_display = ('uid', 'feature_code')


class AssetClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'sub_class')
    filter_horizontal = ('sub_classes',)

    def sub_class(self, obj):
        """ Return list of sub class
        :param obj:
        :type obj: AssetClass
        :return:
        """
        return ', '.join(
            [sub_class.__str__() for sub_class in obj.sub_classes.all()]
        )


class AssetSubClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class FeatureCodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'asset_class', 'asset_sub_class')


admin.site.register(AssetClass, AssetClassAdmin)
admin.site.register(AssetSubClass, AssetSubClassAdmin)
admin.site.register(FeatureCode, FeatureCodeAdmin)


class BaseFeatureAdmin(OSMGeoAdmin):
    default_lon = 11170608.17969
    default_lat = -100436.17209
    default_zoom = 17
    readonly_fields = ('uid',)
    list_filter = ('feature_code',)

    class Meta:
        abstract = True
