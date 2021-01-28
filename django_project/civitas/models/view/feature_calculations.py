__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '11/11/20'

from datetime import datetime
from django.contrib.gis.db import models
from civitas.models.feature.feature_base import FeatureBase


class FeatureCalculation(models.Model):
    """ This is the calculation view of feature"""
    feature = models.OneToOneField(
        FeatureBase,
        on_delete=models.CASCADE,
        primary_key=True
    )
    estimated_renewal_cost = models.FloatField(
        null=True, blank=True,
        help_text='How much cost for renewal the feature with all quantity'
    )
    estimated_annual_maintenance_cost = models.FloatField(
        null=True, blank=True,
        help_text='How much cost to maintenance the feature with all quantity'
    )
    estimated_annual_reserve = models.FloatField(
        null=True, blank=True,
        help_text='How much cost to maintenance the feature with all quantity'
    )
    lifespan = models.FloatField(
        null=True, blank=True
    )

    # Age based
    age = models.FloatField(
        null=True, blank=True
    )
    remaining_years_age_based = models.FloatField(
        null=True, blank=True
    )
    remaining_percent_age_based = models.CharField(
        null=True, blank=True,
        max_length=512
    )
    # Condition based
    remaining_years_condition_based = models.FloatField(
        null=True, blank=True
    )
    remaining_percent_condition_based = models.CharField(
        null=True, blank=True,
        max_length=512
    )

    # Risk
    # TODO:
    #  open it after the column has been added
    # risk_value = models.FloatField(
    #     null=True, blank=True
    # )
    # risk_level = models.TextField(
    #     null=True, blank=True
    # )

    class Meta:
        managed = False
        db_table = 'feature_calculations'

    # Get calculation from data
    def renewal_cost(self):
        """ Estimated renewal cost """
        if self.estimated_renewal_cost is not None:
            return float(self.estimated_renewal_cost)
        return 0

    def maintenance_cost(self):
        """ Estimated maintenance cost """
        if self.estimated_annual_maintenance_cost is not None:
            return float(self.estimated_annual_maintenance_cost)
        return 0

    def annual_reserve_cost(self):
        """ Calculate cost that needed annually"""
        if self.estimated_annual_reserve is not None:
            return float(self.estimated_annual_reserve)
        return 0

    def remaining_life(self):
        """ Remaining life """
        if self.remaining_years_condition_based \
                and self.remaining_years_condition_based is not None:
            return self.remaining_years_condition_based
        if self.remaining_years_age_based \
                and self.remaining_years_age_based is not None:
            return self.remaining_years_age_based
        return None

    def remaining_life_percent(self):
        """ Remaining life in percent"""
        if self.remaining_percent_condition_based \
                and self.remaining_percent_condition_based is not None:
            return self.remaining_percent_condition_based
        if self.remaining_percent_age_based \
                and self.remaining_percent_age_based is not None:
            return self.remaining_percent_age_based
        return None

    def renewal_cost_year(
            self, date: datetime) -> float:
        """
        renewal cost for specific year
        example: current 2020, th_year is 1
        so projected cost is 2021
        """
        # check for maintenance cost
        th_year = date.year - datetime.today().year
        if th_year < 0:
            return 0

        # check for specific cost
        renewal_cost = self.renewal_cost()
        if renewal_cost:
            lifespan = self.lifespan
            remaining_life = self.remaining_life()
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
