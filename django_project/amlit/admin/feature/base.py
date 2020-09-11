__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from amlit.models.feature.base import (
    Condition, Deterioration, FeatureClass,
    FeatureSubClass, FeatureType, FeatureSubType, FeatureTypeCombination
)


class DeteriorationAdmin(admin.ModelAdmin):
    list_display = ('name', 'equation')


class FeatureClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class FeatureSubClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'unit', 'deterioration')


class FeatureTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'maintenance_cost', 'renewal_cost', 'lifespan')


class FeatureTypeCombinationAdmin(admin.ModelAdmin):
    list_display = (
        'the_class', 'sub_class', 'type')


class FeatureSubTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


admin.site.register(Condition)
admin.site.register(Deterioration, DeteriorationAdmin)
admin.site.register(FeatureClass, FeatureClassAdmin)
admin.site.register(FeatureSubClass, FeatureSubClassAdmin)
admin.site.register(FeatureType, FeatureTypeAdmin)
admin.site.register(FeatureSubType, FeatureSubTypeAdmin)
admin.site.register(FeatureTypeCombination, FeatureTypeCombinationAdmin)


class BaseFeatureAdmin(OSMGeoAdmin):
    default_lon = -13271942
    default_lat = 6485105
    default_zoom = 12
    list_display = ('uid', 'type', 'system', 'date_installed', 'remaining_life')
    readonly_fields = (
        'uid', 'age', 'remaining_life', 'remaining_life_percent',
        'replacement_cost', 'maintenance_cost', 'annual_reserve_cost'
    )
    list_filter = ('type__the_class', 'type__sub_class', 'type__type')

    class Meta:
        abstract = True

    def render_change_form(self, request, context, *args, **kwargs):
        # self.model._meta.db_table
        return super(BaseFeatureAdmin, self).render_change_form(
            request, context, *args, **kwargs)
