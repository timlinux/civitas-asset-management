__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '05/03/21'

from django.db import models
from django.utils.translation import ugettext_lazy as _
from helpdesk.models import Ticket


class FeatureTicket(models.Model):
    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, verbose_name=_('ticket'))
    feature_id = models.IntegerField(
        _('feature id'))

    def __str__(self):
        return self.ticket.__str__()
