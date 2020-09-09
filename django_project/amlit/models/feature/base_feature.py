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
    description = models.TextField(
        null=True, blank=True
    )

    # fixed properties
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

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super(BaseFeature, self).save(*args, **kwargs)
        new_uid = '{}-{}-{}-{}'.format(
            self.type.the_class.name,
            self.type.sub_class.name,
            self.type.type.name,
            self.id
        )
        if self.uid != new_uid:
            self.uid = new_uid
            self.save()

    def __str__(self):
        return '{}'.format(self.uid)

    def lifespan(self):
        """ Return lifespan of feature"""
        return self.type.type.lifespan

    def replacement_cost(self):
        """ Calculate replacement cost """
        return self.type.type.renewal_cost.value * self.quantity \
            if self.type.type.renewal_cost else 0

    def maintenance_cost(self):
        """ Calculate maintenance cost """
        return self.type.type.maintenance_cost.value * self.quantity \
            if self.type.type.maintenance_cost else 0

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
            return self.lifespan() * (1 - float(eval(deterioration_eq)))
        if self.lifespan():
            return datetime.today().year - self.date_installed.year
        return None

    def remaining_life(self):
        """ Calculate remaining life """
        age = self.age()
        if age is not None:
            return self.lifespan() - age
        return None

    def remaining_life_percent(self):
        """ Calculate remaining life in percent"""
        remaining_life = self.remaining_life()
        if remaining_life is not None:
            return int(100 * remaining_life / self.lifespan())
        return None

    def annual_reserve_cost(self):
        """ Calculate cost that needed annually"""
        maintenance_cost = self.replacement_cost()
        replacement_cost = self.replacement_cost()
        lifespan = self.lifespan()
        if maintenance_cost and replacement_cost and lifespan:
            return (replacement_cost / lifespan) + maintenance_cost
        return 0

    def replacement_cost_year(self, th_year):
        """
        Replacement cost for specific year
        example: current 2020, th_year is 1
        so projected cost is 2021

        :type th_year: int
        """
        # check for maintenance cost

        # check for specific cost
        replacement_cost = self.replacement_cost()
        if replacement_cost:
            lifespan = self.lifespan()
            remaining_life = self.remaining_life()
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
