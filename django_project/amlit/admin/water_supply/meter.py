__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.admin.base_feature import BaseFeatureAdmin, water_list_display
from amlit.models.water_supply import (
    Meter, MeterType, MeterPID, MeterReadingType
)


class MeterAdmin(BaseFeatureAdmin):
    list_display = water_list_display + (
        'type', 'brand', 'model', 'reading_type', 'pid')


admin.site.register(MeterPID)
admin.site.register(MeterReadingType)
admin.site.register(MeterType)
admin.site.register(Meter, MeterAdmin)
