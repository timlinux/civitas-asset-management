__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from datetime import datetime
from django.contrib.gis.db import models
from amlit.models.feature.base import (
    FeatureTypeCombination, Condition
)
from amlit.models.feature.general import GeneralBrand, GeneralMaterial
from amlit.models.system import System


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
    type = models.ForeignKey(
        FeatureTypeCombination,
        on_delete=models.CASCADE
    )

    date_installed = models.DateField(
        help_text='When this feature is installed'
    )
    quantity = models.FloatField(
        help_text='Quantity of the feature. '
                  'The unit is based on the sub class')
    condition = models.ForeignKey(
        Condition,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        help_text='Condition of the feature'
    )

    # fixed properties
    description = models.TextField(
        null=True, blank=True
    )
    system = models.ForeignKey(
        System,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        help_text='What system the feature belongs to'
    )
    brand = models.ForeignKey(
        GeneralBrand,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    material = models.ForeignKey(
        GeneralMaterial,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )

    # calculated field
    age = models.FloatField(
        null=True, blank=True
    )
    remaining_life = models.FloatField(
        null=True, blank=True,
        help_text='How much remaining life for the feature'
    )
    remaining_life_percent = models.FloatField(
        null=True, blank=True,
        help_text='How much remaining life in percent for the feature'
    )
    annual_reserve_cost = models.FloatField(
        null=True, blank=True,
        help_text='How much cost should be reserved annually'
    )
    replacement_cost = models.FloatField(
        null=True, blank=True,
        help_text='How much cost for replacing the feature with all quantity'
    )
    maintenance_cost = models.FloatField(
        null=True, blank=True,
        help_text='How much cost to maintenance the feature with all quantity'
    )

    class Meta:
        abstract = True

    def __str__(self):
        return '{}'.format(self.uid)

    def save(self, *args, **kwargs):
        new_uid = '{}-{}-{}-{}'.format(
            self.type.the_class.name,
            self.type.sub_class.name,
            self.type.type.name,
            self.id
        )
        if self.uid != new_uid:
            self.uid = new_uid
        self.calculation()
        super(BaseFeature, self).save(*args, **kwargs)

    def lifespan(self):
        """ Return lifespan of feature"""
        return self.type.type.lifespan

    def replacement_cost_year(self, date):
        """
        Replacement cost for specific year
        example: current 2020, th_year is 1
        so projected cost is 2021

        :type date: datetime
        """
        # check for maintenance cost
        th_year = date.year - datetime.today().year
        if th_year < 0:
            return 0

        # check for specific cost
        replacement_cost = self.replacement_cost
        if replacement_cost:
            lifespan = self.lifespan()
            remaining_life = self.remaining_life
            after_renewal = th_year - remaining_life

            # calculate remaining life
            if remaining_life == th_year:
                # this is for first renewal
                # Example: remaining life is 5
                # if th_year is 5, it is replacement state
                return replacement_cost
            if after_renewal % lifespan == 0:
                # this is for every renewal cost after first renewal
                # Example: remaining life is 5
                # lifespan is 6
                # if th_year is 11, it is replacement state (remaining life + lifespan)
                # if th_year is 17, it is replacement state (remaining life + lifespan*2)
                return replacement_cost
        return 0

    def calculation(self):
        """ Calculate all field that needs calculation"""
        calculation = BaseFeatureCalculation(self)
        self.age = calculation.age()
        self.remaining_life = calculation.remaining_life()
        self.remaining_life_percent = calculation.remaining_life_percent()
        self.annual_reserve_cost = calculation.annual_reserve_cost()
        self.replacement_cost = calculation.replacement_cost()
        self.maintenance_cost = calculation.maintenance_cost()


class BaseFeatureCalculation(object):
    def __init__(self, feature):
        self.feature = feature

    def replacement_cost(self):
        """ Calculate replacement cost """
        return self.feature.type.type.renewal_cost.value * self.feature.quantity \
            if self.feature.type.type.renewal_cost else 0

    def maintenance_cost(self):
        """ Calculate maintenance cost """
        return self.feature.type.type.maintenance_cost.value * self.feature.quantity \
            if self.feature.type.type.maintenance_cost else 0

    # function for reports
    def age(self):
        """ Calculate age
        If condition presented, use condition for age
        else use installed year
        """
        if self.feature.condition:
            condition = self.feature.condition.value
            deterioration_eq = self.feature.type.sub_class.deterioration.equation
            deterioration_eq = deterioration_eq.replace(
                'x', str(condition)).replace(
                '^', '**').replace(
                'Y=', ''
            )
            return self.feature.lifespan() * (1 - float(eval(deterioration_eq)))
        if self.feature.lifespan():
            return datetime.today().year - self.feature.date_installed.year
        return None

    # TODO:
    #  save these functions to database
    def remaining_life(self):
        """ Calculate remaining life """
        age = self.age()
        if age is not None:
            return self.feature.lifespan() - age
        return None

    def remaining_life_percent(self):
        """ Calculate remaining life in percent"""
        remaining_life = self.remaining_life()
        if remaining_life is not None:
            return int(100 * remaining_life / self.feature.lifespan())
        return None

    def annual_reserve_cost(self):
        """ Calculate cost that needed annually"""
        maintenance_cost = self.maintenance_cost()
        replacement_cost = self.replacement_cost()
        lifespan = self.feature.lifespan()
        if maintenance_cost and replacement_cost and lifespan:
            return (replacement_cost / lifespan) + maintenance_cost
        return 0
