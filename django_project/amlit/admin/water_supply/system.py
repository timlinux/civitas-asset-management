__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.models.water_supply.system import WaterSystem


class WaterSystemAdmin(admin.ModelAdmin):
    filter_horizontal = (
        'boxes', 'chambers', 'controls', 'hydrants', 'meters',
        'motors', 'parts', 'pipes', 'pumps', 'sources', 'tanks', 'valves')


admin.site.register(WaterSystem, WaterSystemAdmin)
