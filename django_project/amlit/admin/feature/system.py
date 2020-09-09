__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.models.system import System


class WaterSystemAdmin(admin.ModelAdmin):
    pass


admin.site.register(System, WaterSystemAdmin)
