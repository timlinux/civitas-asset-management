__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/08/20'

from amlit.models.abstract import _Term


class GeneralBrand(_Term):
    """ List of Brand for feature."""

    class Meta:
        db_table = 'general_brand'


class GeneralMaterial(_Term):
    """ List of material for feature."""

    class Meta:
        db_table = 'general_material'
