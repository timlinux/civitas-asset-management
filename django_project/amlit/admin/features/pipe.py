__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.admin.base_feature import BaseFeatureAdmin, feature_display
from amlit.models.features import Pipe


class PipeAdmin(BaseFeatureAdmin):
    list_display = feature_display + (
        'brand', 'model', 'material',
        'diameter', 'length', 'depth')


admin.site.register(Pipe, PipeAdmin)
