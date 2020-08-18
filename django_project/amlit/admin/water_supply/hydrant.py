__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.admin.base_feature import BaseFeatureAdmin, water_list_display
from amlit.models.water_supply import (
    Hydrant, HydrantType
)


class HydrantAdmin(BaseFeatureAdmin):
    list_display = water_list_display + (
        'type', 'brand', 'model')


admin.site.register(HydrantType)
admin.site.register(Hydrant, HydrantAdmin)
