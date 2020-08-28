__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.admin.base_feature import BaseFeatureAdmin, feature_display
from amlit.models.features import CatchbasinTrunk


class CatchbasinTrunkAdmin(BaseFeatureAdmin):
    list_display = feature_display


admin.site.register(CatchbasinTrunk, CatchbasinTrunkAdmin)
