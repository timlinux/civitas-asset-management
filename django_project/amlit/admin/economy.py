__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.models.economy import Currency, Money

admin.site.register(Currency)
admin.site.register(Money)
