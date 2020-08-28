__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from amlit.models.base_feature import (
    FeatureClass, FeatureSubClass, FeatureCode, FeatureType, FeatureSubType
)

feature_display = ('uid', 'type', 'system', 'date_installed', 'remaining_life')


class FeatureClassAdmin(admin.ModelAdmin):
    list_display = ('name',)


class FeatureSubClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'the_class')


class FeatureTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'sub_class', 'the_class',
        'maintenance_cost', 'renewal_cost', 'lifespan', 'unit')
    list_filter = ('sub_class', 'sub_class__the_class')

    def the_class(self, obj):
        """ Return the_class
        :param obj:
        :return:
        """
        return obj.sub_class.the_class.__str__()

    the_class.short_description = 'class'


class FeatureSubTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


class FeatureCodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub_class')


admin.site.register(FeatureClass, FeatureClassAdmin)
admin.site.register(FeatureSubClass, FeatureSubClassAdmin)
admin.site.register(FeatureType, FeatureTypeAdmin)
admin.site.register(FeatureSubType, FeatureSubTypeAdmin)
admin.site.register(FeatureCode, FeatureCodeAdmin)


class BaseFeatureAdmin(OSMGeoAdmin):
    default_lon = 11170608.17969
    default_lat = -100436.17209
    default_zoom = 17
    readonly_fields = ('uid', 'feature_code', 'remaining_life')
    list_filter = ('type',)

    class Meta:
        abstract = True

    def remaining_life(self, obj):
        """ Return remaining_life
        """
        return '{} years'.format(obj.remaining_life())
