__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '05/04/21'

from datetime import date
from dateutil.relativedelta import relativedelta
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from amlit.models.organisation import Organisation
from core.models.term import TermModel


class Currency(TermModel):
    """
    Currency for price
    """
    code = models.CharField(
        _('Code'), max_length=8)


class Plan(TermModel):
    """
    Permissions plan of subscription
    Contains settings for subscription
    """

    # this is subscription settings
    max_user = models.IntegerField(_('Max user'))


class SubscriptionPlan(models.Model):
    """
    This is the plan for subscription
    """
    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE,
        verbose_name=_('Plan')
    )

    ANNUALLY = 'annually'
    MONHTLY = 'monthly'
    SUBSCRIPTION_PLAN_TIME = [
        (MONHTLY, 'Monthly'),
        (ANNUALLY, 'Annually'),
    ]

    price = models.FloatField(_('Price'))
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        verbose_name=_('Currency')
    )
    time_plan = models.CharField(
        max_length=64,
        choices=SUBSCRIPTION_PLAN_TIME,
        default=ANNUALLY,
    )

    def __str__(self):
        return '{} ({})'.format(self.plan, self.time_plan)


class Subscription(models.Model):
    """
    This is subscription for an organisation
    Just active at one time
    """
    organisation = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE,
        verbose_name=_('Organisation'),
        related_name='subscription_organisation'
    )
    ACTIVE = 'active'
    CANCELED = 'canceled'
    EXPIRED = 'expired'
    STATUS = [
        (ACTIVE, 'Active'),
        (CANCELED, 'Canceled'),
        (EXPIRED, 'Expired'),
    ]
    status = models.CharField(
        max_length=64,
        choices=STATUS,
        default=ACTIVE,
    )
    subscription_plan = models.ForeignKey(
        SubscriptionPlan,
        on_delete=models.CASCADE,
        verbose_name=_('Subscription plan')
    )
    date_subscribed = models.DateField(
        _('Date subscribed'),
        default=date.today
    )
    date_expired = models.DateField(
        _('Date expired'),
        null=True, blank=True
    )

    def save(self, *args, **kwargs):
        # fill expired date
        if self.subscription_plan.time_plan == SubscriptionPlan.ANNUALLY:
            self.date_expired = self.date_subscribed + relativedelta(years=1)
        elif self.subscription_plan.time_plan == SubscriptionPlan.MONHTLY:
            self.date_expired = self.date_subscribed + relativedelta(months=1)

        super(Subscription, self).save(*args, **kwargs)
        if self.status == self.ACTIVE:
            self.organisation.subscription = self
            self.organisation.save()

    def __str__(self):
        return self.subscription_plan.__str__()
