__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from aim.models.water_supply import (
    Tank, TankBrand, TankType
)


class TankAdmin(admin.ModelAdmin):
    list_display = ('uid', 'type', 'brand', 'model', 'capacity', 'feature_code')


admin.site.register(TankBrand)
admin.site.register(TankType)
admin.site.register(Tank, TankAdmin)
