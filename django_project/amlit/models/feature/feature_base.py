__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from datetime import datetime
from django.contrib.gis.db import models
from amlit.models.feature.identifier import (
    Condition, FeatureClass, FeatureSubClass, FeatureType
)
from amlit.models.community import System
from amlit.models.others import AimsoirFeatureCode, COF, POF


class FeatureBase(models.Model):
    """
    Model for base feature.
    Every feature needs to override this model
    """

    install_date = models.DateField(
        help_text='When this feature is installed'
    )
    quantity = models.FloatField(
        help_text='Quantity of the feature. '
                  'The unit is based on the sub class')
    description = models.TextField(
        null=True, blank=True
    )
    the_class = models.ForeignKey(
        FeatureClass,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        db_column='class_id',
        verbose_name='class'
    )
    sub_class = models.ForeignKey(
        FeatureSubClass,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    type = models.ForeignKey(
        FeatureType,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    system = models.ForeignKey(
        System,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        help_text='What system the feature belongs to'
    )
    pof = models.ForeignKey(
        POF,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        db_column='pof',
        verbose_name='pof'
    )
    cof = models.ForeignKey(
        COF,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        db_column='cof',
        verbose_name='cof'
    )
    aimsoir_feature_code = models.ForeignKey(
        AimsoirFeatureCode,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        db_column='aimsoir_feature_code'
    )
    capital_project_id = models.SmallIntegerField(
        null=True, blank=True
    )

    # calculated field
    condition = models.ForeignKey(
        Condition,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        help_text='Condition of the feature'
    )

    # TODO:
    #  uncomment this after data in database already filled
    # renewal_cost = models.FloatField(
    #     null=True, blank=True,
    #     help_text='How much cost for renewal the feature with all quantity'
    # )
    # maintenance_cost = models.FloatField(
    #     null=True, blank=True,
    #     help_text='How much cost to maintenance the feature with all quantity'
    # )

    # others
    file_reference = models.TextField(
        null=True, blank=True
    )
    view_name = models.TextField(
        null=True, blank=True
    )

    class Meta:
        managed = False
        db_table = 'feature_base'

    def save(self, *args, **kwargs):
        super(FeatureBase, self).save(*args, **kwargs)

    def lifespan(self):
        """ Return lifespan of feature"""
        if not self.type:
            return None
        return self.type.lifespan

    def renewal_cost_year(
            self, date: datetime) -> float:
        """
        renewal cost for specific year
        example: current 2020, th_year is 1
        so projected cost is 2021
        """
        calculation = BaseFeatureCalculation(self)
        # check for maintenance cost
        th_year = date.year - datetime.today().year
        if th_year < 0:
            return 0

        # check for specific cost
        renewal_cost = calculation.renewal_cost()
        if renewal_cost:
            lifespan = self.lifespan()
            remaining_life = calculation.remaining_life()
            after_renewal = th_year - remaining_life

            # calculate remaining life
            if remaining_life == th_year:
                # this is for first renewal
                # Example: remaining life is 5
                # if th_year is 5, it is renewal state
                return renewal_cost
            if after_renewal % lifespan == 0:
                # this is for every renewal cost after first renewal
                # Example: remaining life is 5
                # lifespan is 6
                # if th_year is 11, it is renewal state (remaining life + lifespan)
                # if th_year is 17, it is renewal state (remaining life + lifespan*2)
                return renewal_cost
        return 0

    def calculation(self):
        """ Calculate all field that needs calculation"""
        return BaseFeatureCalculation(self)


class BaseFeatureCalculation(object):
    def __init__(self, feature):
        self.feature = feature

    def renewal_cost(self):
        """ Calculate renewal cost """
        if not self.feature.type:
            return 0
        return self.feature.type.renewal_cost * self.feature.quantity \
            if self.feature.type.renewal_cost and self.feature.quantity else 0

    def maintenance_cost(self):
        """ Calculate maintenance cost """
        if not self.feature.type:
            return 0
        return self.feature.type.maintenance_cost * self.feature.quantity \
            if self.feature.type.maintenance_cost and self.feature.quantity else 0

    # function for reports
    def age(self):
        """ Calculate age
        If condition presented, use condition for age
        else use installed year
        """
        if self.feature.condition:
            condition = self.feature.condition.value
            deterioration_eq = self.feature.sub_class.deterioration.equation
            deterioration_eq = deterioration_eq.replace(
                'x', str(condition)).replace(
                '^', '**').replace(
                'Y=', ''
            )
            if self.feature.lifespan():
                return self.feature.lifespan() * (1 - float(eval(deterioration_eq)))
        if self.feature.lifespan() and self.feature.install_date:
            return datetime.today().year - self.feature.install_date.year
        return None

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
        renewal_cost = self.renewal_cost()
        lifespan = self.feature.lifespan()
        if maintenance_cost and renewal_cost and lifespan:
            return (renewal_cost / lifespan) + maintenance_cost
        return 0
