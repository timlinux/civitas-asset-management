__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.admin.base_feature import BaseFeatureAdmin
from amlit.models.water_supply import (
    Pipe, PipeType
)


class PipeAdmin(BaseFeatureAdmin):
    list_display = (
        'uid', 'type', 'brand', 'model', 'material',
        'diameter', 'length', 'depth', 'feature_code')


admin.site.register(PipeType)
admin.site.register(Pipe, PipeAdmin)
