__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/08/20'

from django.contrib import admin
from amlit.models.water_supply import (
    WaterGeneralBrand, WaterGeneralMaterial)

admin.site.register(WaterGeneralBrand)
admin.site.register(WaterGeneralMaterial)
