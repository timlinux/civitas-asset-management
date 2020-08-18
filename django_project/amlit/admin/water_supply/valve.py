__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.admin.base_feature import BaseFeatureAdmin, water_list_display
from amlit.models.water_supply import (
    Valve, ValveType, ValveActuationDirection, ValveActuationSpec, ValveActuationType
)


class ValveAdmin(BaseFeatureAdmin):
    list_display = water_list_display + (
        'type', 'brand', 'model', 'depth')


admin.site.register(ValveType)
admin.site.register(ValveActuationDirection)
admin.site.register(ValveActuationSpec)
admin.site.register(ValveActuationType)
admin.site.register(Valve, ValveAdmin)
