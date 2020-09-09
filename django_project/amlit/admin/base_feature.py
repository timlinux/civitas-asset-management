__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from amlit.models.base_feature import (
    Condition, Deterioration, FeatureClass, FeatureSubClass, FeatureCode, FeatureType, FeatureSubType
)

feature_display = ('uid', 'type', 'system', 'date_installed', 'remaining_life')


class DeteriorationAdmin(admin.ModelAdmin):
    list_display = ('name', 'equation')


class FeatureClassAdmin(admin.ModelAdmin):
    list_display = ('name',)


class FeatureSubClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'the_class', 'unit', 'deterioration')


class FeatureTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'sub_class', 'the_class',
        'maintenance_cost', 'renewal_cost', 'lifespan')
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


admin.site.register(Condition)
admin.site.register(Deterioration, DeteriorationAdmin)
admin.site.register(FeatureClass, FeatureClassAdmin)
admin.site.register(FeatureSubClass, FeatureSubClassAdmin)
admin.site.register(FeatureType, FeatureTypeAdmin)
admin.site.register(FeatureSubType, FeatureSubTypeAdmin)
admin.site.register(FeatureCode, FeatureCodeAdmin)


class BaseFeatureAdmin(OSMGeoAdmin):
    default_lon = 11170608.17969
    default_lat = -100436.17209
    default_zoom = 17
    readonly_fields = (
        'uid', 'feature_code', 'age', 'remaining_life_percent',
        'replacement_cost', 'maintenance_cost', 'annual_reserve_cost'
    )
    list_filter = ('type',)

    class Meta:
        abstract = True

    def age(self, obj):
        """ Return age
        """
        return '{} years'.format(obj.age())

    def remaining_life(self, obj):
        """ Return remaining_life
        """
        return '{} years'.format(obj.remaining_life())

    def replacement_cost(self, obj):
        """ Return replacement_cost
        """
        return '{} {}'.format(obj.type.renewal_cost.currency, obj.replacement_cost())

    def maintenance_cost(self, obj):
        """ Return replacement_cost
        """
        return '{} {}'.format(obj.type.renewal_cost.currency, obj.maintenance_cost())

    def remaining_life_percent(self, obj):
        """ Return remaining_life_percent
        """
        return '{}%'.format(obj.remaining_life_percent())

    def annual_reserve_cost(self, obj):
        """ Return annual_reserve_cost
        """
        return '{} {}'.format(obj.type.renewal_cost.currency, obj.annual_reserve_cost())
