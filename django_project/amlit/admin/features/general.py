__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/08/20'

from django.contrib import admin
from amlit.models.features import (
    GeneralBrand, GeneralMaterial)

admin.site.register(GeneralBrand)
admin.site.register(GeneralMaterial)
