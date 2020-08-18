__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.admin.base_feature import BaseFeatureAdmin
from amlit.models.water_supply import (
    Part, PartType
)


class PartAdmin(BaseFeatureAdmin):
    list_display = (
        'uid', 'type', 'brand', 'model', 'material', 'depth', 'feature_code')


admin.site.register(PartType)
admin.site.register(Part, PartAdmin)
