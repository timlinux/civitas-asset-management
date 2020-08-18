__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.admin.base_feature import BaseFeatureAdmin
from amlit.models.water_supply import (
    Meter, MeterType
)


class MeterAdmin(BaseFeatureAdmin):
    list_display = (
        'uid', 'type', 'brand', 'model', 'reading_type', 'pid', 'feature_code')


admin.site.register(MeterType)
admin.site.register(Meter, MeterAdmin)
