__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '05/03/21'

from django.contrib import admin
from amlit_helpdesk.models.feature_ticket import FeatureTicket


class FeatureTicketAdmin(admin.ModelAdmin):
    list_display = ('feature_id', 'ticket')
    list_filter = ('feature_id',)


admin.site.register(FeatureTicket, FeatureTicketAdmin)
