__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.admin.base_feature import BaseFeatureAdmin
from amlit.models.water_supply import Box


class BoxAdmin(BaseFeatureAdmin):
    list_display = (
        'uid', 'brand', 'model', 'material', 'feature_code')


admin.site.register(Box, BoxAdmin)
