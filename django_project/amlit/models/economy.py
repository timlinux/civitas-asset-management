__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '27/08/20'

from django.contrib.gis.db import models
from amlit.models.abstract import _Term


class Currency(_Term):
    """ Currency """
    code = models.CharField(max_length=512)

    class Meta:
        ordering = ('name',)
        db_table = 'currency'

    def __str__(self):
        return self.code


class Money(models.Model):
    """ Money with Specific Currency """
    value = models.FloatField()
    currency = models.ForeignKey(
        Currency,
        blank=True, null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        db_table = 'money'

    def __str__(self):
        return '{} {}'.format(self.value, self.currency)
