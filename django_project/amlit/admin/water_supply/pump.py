__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.admin.base_feature import BaseFeatureAdmin
from amlit.models.water_supply import (
    Pump, PumpBrand, PumpType, PumpSubType
)


class PumpAdmin(BaseFeatureAdmin):
    list_display = (
        'uid', 'subtype', 'brand', 'model',
        'submerged', 'capacity', 'head', 'feature_code')


admin.site.register(PumpBrand)
admin.site.register(PumpType)
admin.site.register(PumpSubType)
admin.site.register(Pump, PumpAdmin)
