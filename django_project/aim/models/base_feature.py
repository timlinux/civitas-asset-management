__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib.gis.db import models
from aim.models.base import _Term


class AssetSubClass(_Term):
    """
    The second Level of the Asset Hierrarchy as defined in "Background" Sheet
    ie. RD = Roads
    It is linked with AssetClass
    """

    class Meta:
        db_table = "asset_sub_class"

    def __str__(self):
        return '({}) {}'.format(self.name, self.description)


class AssetClass(_Term):
    """
    The first Level of the Asset Hierrarchy as defined in "Background" Sheet
    ie. TRN = Transportation
    """
    sub_classes = models.ManyToManyField(
        AssetSubClass, blank=True
    )

    class Meta:
        db_table = "asset_class"

    def __str__(self):
        return '({}) {}'.format(self.name, self.description)


class FeatureCode(_Term):
    """
    Feature code as defined in "Background" Sheet
    ie. CB = Stormwater Catch Basin
    It is linked with AssetSubClass
    """

    asset_class = models.ForeignKey(
        AssetClass, on_delete=models.CASCADE)
    asset_sub_class = models.ForeignKey(
        AssetSubClass, on_delete=models.CASCADE)

    class Meta:
        db_table = "feature_code"

    def __str__(self):
        return '({}) {}'.format(self.name, self.description)


class BaseFeature(models.Model):
    """
    Model for base feature.
    Every feature needs to override this model
    """

    uid = models.CharField(
        max_length=256,
        null=True, blank=True,
        help_text='unique asset ID'
    )
    description = models.TextField(
        null=True, blank=True
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super(BaseFeature, self).save(*args, **kwargs)
        new_uid = '{}-{}-{}-{}'.format(
            self.get_feature_code().asset_class.name,
            self.get_feature_code().asset_sub_class.name,
            self.get_feature_code().name,
            self.id
        )
        if self.uid != new_uid:
            self.uid = new_uid
            self.save()

    def get_feature_code(self):
        """
        return current feature code
        :rtype: FeatureCode
        """
        raise NotImplementedError

    def __str__(self):
        return '{}'.format(self.uid)
