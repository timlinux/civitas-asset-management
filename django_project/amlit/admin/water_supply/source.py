__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.admin.base_feature import BaseFeatureAdmin
from amlit.models.water_supply import (
    Source, SourceType
)


class SourceAdmin(BaseFeatureAdmin):
    list_display = ('uid', 'type', 'feature_code')


admin.site.register(SourceType)
admin.site.register(Source, SourceAdmin)
