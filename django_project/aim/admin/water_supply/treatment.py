__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from aim.admin.base_feature import BaseFeatureAdmin
from aim.models.water_supply import (
    Treatment, TreatmentType
)


class TreatmentAdmin(BaseFeatureAdmin):
    list_display = ('uid', 'type', 'feature_code')


admin.site.register(TreatmentType)
admin.site.register(Treatment, TreatmentAdmin)
