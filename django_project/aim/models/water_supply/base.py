__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from aim.models.base_feature import BaseFeature, FeatureCode


class WaterSupplyFeature(BaseFeature):
    """
    Model for water supply feature.
    Every water supply feature needs to override this model
    """

    feature_code = models.ForeignKey(
        FeatureCode, on_delete=models.CASCADE,
        limit_choices_to={
            'asset_class__name': 'PWS'}
    )

    def get_feature_code(self):
        """
        return current feature code
        :rtype: FeatureCode
        """
        return self.feature_code

    class Meta:
        ordering = ('feature_code__name',)
        abstract = True
