__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.admin.base_feature import BaseFeatureAdmin, feature_display
from amlit.models.features import (
    Meter, MeterPID, MeterReadingType
)


class MeterAdmin(BaseFeatureAdmin):
    list_display = feature_display + (
        'brand', 'model', 'reading_type', 'pid')


admin.site.register(MeterPID)
admin.site.register(MeterReadingType)
admin.site.register(Meter, MeterAdmin)
