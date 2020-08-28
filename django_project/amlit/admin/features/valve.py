__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.admin.base_feature import BaseFeatureAdmin, feature_display
from amlit.models.features import (
    Valve, ValveActuationDirection, ValveActuationSpec, ValveActuationType
)


class ValveAdmin(BaseFeatureAdmin):
    list_display = feature_display + (
        'brand', 'model', 'depth')


admin.site.register(ValveActuationDirection)
admin.site.register(ValveActuationSpec)
admin.site.register(ValveActuationType)
admin.site.register(Valve, ValveAdmin)
