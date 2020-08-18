__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/08/20'

from amlit.models.base import _Term


class WaterGeneralBrand(_Term):
    """ List of Brand for water."""

    class Meta:
        db_table = 'water_general_brand'


class WaterGeneralMaterial(_Term):
    """ List of material for water."""

    class Meta:
        db_table = 'water_general_material'
