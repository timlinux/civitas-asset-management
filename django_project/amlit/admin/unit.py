__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.models.unit import Unit, Quantity

admin.site.register(Unit)
admin.site.register(Quantity)
