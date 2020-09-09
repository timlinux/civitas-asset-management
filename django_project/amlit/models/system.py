__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/08/20'

from django.contrib.gis.db import models
from amlit.models.abstract import _Term
from amlit.models.community import Community


class System(_Term):
    """
     System is a collection of all of feature
    """
    community = models.ForeignKey(
        Community, blank=True, null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        db_table = 'system'
