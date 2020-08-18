__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.admin.base_feature import BaseFeatureAdmin
from amlit.models.water_supply import (
    Tank, TankType
)


class TankAdmin(BaseFeatureAdmin):
    list_display = ('uid', 'type', 'brand', 'model', 'capacity', 'feature_code')


admin.site.register(TankType)
admin.site.register(Tank, TankAdmin)
