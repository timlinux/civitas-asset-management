__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.admin.base_feature import BaseFeatureAdmin, water_list_display
from amlit.models.water_supply import (
    Pump, PumpType, PumpSubType
)


class PumpAdmin(BaseFeatureAdmin):
    list_display = water_list_display + (
        'subtype', 'brand', 'model',
        'submerged', 'capacity', 'head')


admin.site.register(PumpType)
admin.site.register(PumpSubType)
admin.site.register(Pump, PumpAdmin)
