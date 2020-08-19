__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.models.water_supply.system import WaterSystem


class WaterSystemAdmin(admin.ModelAdmin):
    filter_horizontal = (
        'boxes', 'chamber', 'control', 'hydrant', 'meter',
        'motor', 'part', 'pipe', 'pump', 'source', 'tank', 'valve')


admin.site.register(WaterSystem, WaterSystemAdmin)
