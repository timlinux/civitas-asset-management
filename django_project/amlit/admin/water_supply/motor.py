__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.admin.base_feature import BaseFeatureAdmin
from amlit.models.water_supply import (
    Motor, MotorType
)


class MotorAdmin(BaseFeatureAdmin):
    list_display = (
        'uid', 'model', 'type', 'output_hp', 'output_power', 'feature_code')


admin.site.register(MotorType)
admin.site.register(Motor, MotorAdmin)
