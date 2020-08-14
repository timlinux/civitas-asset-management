__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models


class _Administrative(models.Model):
    """
    Administrative object
    """
    code = models.CharField(
        unique=True,
        max_length=128,
        help_text='Administrative code'
    )
    name = models.CharField(max_length=512)
    description = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '({}) {}'.format(self.code, self.name)


class Province(_Administrative):
    """
    Administrative province
    """

    class Meta:
        db_table = 'province'


class Region(_Administrative):
    """
    Administrative region
    """

    province = models.ForeignKey(
        Province, on_delete=models.CASCADE)

    class Meta:
        db_table = 'region'


class Community(_Administrative):
    """
    Administrative community
    """

    region = models.ForeignKey(
        Region, on_delete=models.CASCADE)

    class Meta:
        db_table = 'community'
