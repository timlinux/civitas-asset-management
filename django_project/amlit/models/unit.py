__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '27/08/20'

from django.contrib.gis.db import models
from amlit.models.abstract import _Term


class Unit(_Term):
    """ Unit """

    class Meta:
        ordering = ('name',)
        db_table = 'unit'

    def __str__(self):
        return self.name


class Quantity(models.Model):
    """ Value with unit """
    value = models.FloatField()
    unit = models.ForeignKey(
        Unit,
        blank=True, null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        db_table = 'quantity'

    def __str__(self):
        return '{} {}'.format(self.value, self.unit)
