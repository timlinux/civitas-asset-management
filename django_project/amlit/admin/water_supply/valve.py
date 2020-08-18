__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.admin.base_feature import BaseFeatureAdmin
from amlit.models.water_supply import (
    Valve, ValveType, ValveActuationDirection, ValveActuationSpec, ValveActuationType
)


class ValveAdmin(BaseFeatureAdmin):
    list_display = (
        'uid', 'type', 'brand', 'model', 'depth', 'feature_code')


admin.site.register(ValveType)
admin.site.register(ValveActuationDirection)
admin.site.register(ValveActuationSpec)
admin.site.register(ValveActuationType)
admin.site.register(Valve, ValveAdmin)
