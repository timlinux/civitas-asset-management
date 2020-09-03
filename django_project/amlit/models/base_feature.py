__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from datetime import datetime
from django.contrib.gis.db import models
from amlit.models.abstract import _Term
from amlit.models.economy import Money
from amlit.models.unit import Unit, Quantity
from amlit.models.system import System


class Deterioration(_Term):
    """
    The process of becoming progressively worse.
    Contains name and the equation
    """
    equation = models.CharField(max_length=512)

    class Meta:
        ordering = ('name',)
        db_table = 'deterioration'

    def __str__(self):
        return self.name


class Condition(_Term):
    """
    Condition of feature
    1	very good
    2	good
    3	fair
    4	poor
    5	very poor
    """
    value = models.IntegerField()

    class Meta:
        ordering = ('name',)
        db_table = 'condition'

    def __str__(self):
        return self.name


class FeatureClass(_Term):
    """
    The first Level of the Asset Hierarchy as defined in "Background" Sheet
    ie. TRN = Transportation
    """

    class Meta:
        ordering = ('name',)
        db_table = 'feature_class'

    def __str__(self):
        return self.name


class FeatureSubClass(_Term):
    """
    The second Level of the Asset Hierarchy as defined in "Background" Sheet
    ie. RD = Roads
    It is linked with AssetClass
    """
    the_class = models.ForeignKey(
        FeatureClass,
        on_delete=models.CASCADE,
        db_column='class',
        verbose_name='class'
    )
    unit = models.ForeignKey(
        Unit,
        blank=True, null=True,
        on_delete=models.SET_NULL,
        help_text='Default unit for this sub_class'
    )
    deterioration = models.ForeignKey(
        Deterioration,
        blank=True, null=True,
        on_delete=models.SET_NULL,
        help_text='Deterioration of this sub class'
    )

    class Meta:
        ordering = ('name',)
        db_table = 'feature_sub_class'

    def __str__(self):
        return self.name


# This is the new system
class FeatureType(_Term):
    """
    The third Level of the Asset Hierarchy as defined in "Background" Sheet
    """
    sub_class = models.ForeignKey(
        FeatureSubClass,
        on_delete=models.CASCADE
    )

    # This is information for the feature type
    lifespan = models.FloatField(
        blank=True, null=True,
        help_text='Total estimated life span of asset in years'
    )
    maintenance_cost = models.OneToOneField(
        Money,
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='type_maintenance_cost',
        help_text='Annual operation and maintenance cost (Default in canadian dollars)'
    )
    renewal_cost = models.OneToOneField(
        Money,
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='type_renewal_cost',
        help_text='Renewal cost (Default in canadian dollars)'
    )

    class Meta:
        ordering = ('sub_class__the_class', 'sub_class', 'name')
        db_table = 'asset_type'

    def __str__(self):
        return '{} - {} - {}'.format(
            self.sub_class.the_class, self.sub_class, self.name, )


class FeatureSubType(_Term):
    """
    The fourth Level of the Asset Hierarchy as defined in "Background" Sheet
    """
    type = models.ForeignKey(
        FeatureType,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('name',)
        db_table = 'asset_sub_type'

    def __str__(self):
        return self.name


# This is the old system and this is still used
# TODO:
#   need a converter to convert feature code to type/subtype
class FeatureCode(_Term):
    """
    Feature code as defined in "Background" Sheet
    ie. CB = Stormwater Catch Basin
    It is linked with AssetSubClass
    """

    sub_class = models.ForeignKey(
        FeatureSubClass, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        db_table = 'feature_code'

    def __str__(self):
        return self.name


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

    system = models.ForeignKey(
        System,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        help_text='What system the feature belongs to'
    )
    type = models.ForeignKey(
        FeatureType,
        on_delete=models.CASCADE
    )

    sub_type = models.ForeignKey(
        FeatureSubType,
        null=True, blank=True,
        on_delete=models.SET_NULL,
    )
    date_installed = models.DateField(
        help_text='When this feature is installed'
    )
    quantity = models.OneToOneField(
        Quantity,
        on_delete=models.CASCADE,
        help_text='Quantity of the feature'
    )
    condition = models.ForeignKey(
        Condition,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        help_text='Condition of the feature'
    )

    # old system
    feature_code = models.ForeignKey(
        FeatureCode,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    description = models.TextField(
        null=True, blank=True
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super(BaseFeature, self).save(*args, **kwargs)
        new_uid = '{}-{}-{}-{}'.format(
            self.type.sub_class.the_class.name,
            self.type.sub_class.name,
            self.type.name,
            self.id
        )
        if self.uid != new_uid:
            self.uid = new_uid
            self.save()

    def __str__(self):
        return '{}'.format(self.uid)

    # function for reports
    def age(self):
        """ Calculate age
        If condition presented, use condition for age
        else use installed year
        """
        if self.condition:
            condition = self.condition.value
            deterioration_eq = self.type.sub_class.deterioration.equation
            deterioration_eq = deterioration_eq.replace(
                'x', str(condition)).replace(
                '^', '**').replace(
                'Y=', ''
            )
            return self.type.lifespan * float(eval(deterioration_eq))
        if self.type.lifespan:
            return datetime.today().year - self.date_installed.year
        return None

    def remaining_life(self):
        """ Calculate remaining life """
        age = self.age()
        if age:
            return self.type.lifespan - age
        return None

    def replacement_cost(self):
        """ Calculate replacement cost """
        if self.type.renewal_cost:
            return self.type.renewal_cost.value * self.quantity.value
        return None

    def maintenance_cost(self):
        """ Calculate maintenance cost """
        if self.type.maintenance_cost:
            return self.type.maintenance_cost.value * self.quantity.value
        return None

    def remaining_life_percent(self):
        """ Calculate remaining life in percent"""
        age = self.age()
        if age:
            return int(100 * age / self.type.lifespan)
        return None

    def annual_reserve_cost(self):
        """ Calculate cost that needed annually"""
        maintenance_cost = self.replacement_cost()
        replacement_cost = self.replacement_cost()
        lifespan = self.type.lifespan
        if maintenance_cost and replacement_cost and lifespan:
            return (replacement_cost / lifespan) + maintenance_cost
        return None
