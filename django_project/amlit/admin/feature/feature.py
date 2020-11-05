__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '09/09/20'

from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from amlit.models.feature.feature_base import FeatureBase
from amlit.models.feature.feature_geometry import FeatureGeometry
from amlit.models.feature.feature_property import FeatureProperty


class FeaturePropertyPropertyInline(admin.TabularInline):
    model = FeatureProperty


class FeatureBaseAdmin(admin.ModelAdmin):
    list_display = (
        'type', 'system', 'install_date')
    readonly_fields = (
        'renewal_cost', 'maintenance_cost', 'age',
        'remaining_life', 'remaining_life_percent', 'annual_reserve_cost'
    )
    list_filter = ('the_class', 'sub_class', 'type')
    inlines = [FeaturePropertyPropertyInline]

    # TODO:
    #  after these fields already uncommented, remove these
    # CALCULATION
    def renewal_cost(self, obj):
        """ return renewal cost based on calculation"""
        return obj.calculation().renewal_cost()

    def maintenance_cost(self, obj):
        """ return maintenance cost based on calculation"""
        return obj.calculation().maintenance_cost()

    def age(self, obj):
        """ return age based on calculation"""
        return obj.calculation().age()

    def remaining_life(self, obj):
        """ return remaining life based on calculation"""
        return obj.calculation().remaining_life()

    def remaining_life_percent(self, obj):
        """ return remaining life percent based on calculation"""
        return obj.calculation().remaining_life_percent()

    def annual_reserve_cost(self, obj):
        """ return annual reserve cost based on calculation"""
        return obj.calculation().annual_reserve_cost()


class FeatureGeometryAdmin(OSMGeoAdmin):
    default_lon = -13271942
    default_lat = 6485105
    default_zoom = 12


admin.site.register(FeatureBase, FeatureBaseAdmin)
admin.site.register(FeatureGeometry, FeatureGeometryAdmin)
