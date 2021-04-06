__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.models import Subscription, SubscriptionPlan, Plan, Currency


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description')


class SubscriptionPlanInline(admin.TabularInline):
    list_display = ('price', 'currency', 'time_plan')
    model = SubscriptionPlan
    extra = 1


class PlanAdmin(admin.ModelAdmin):
    inlines = (SubscriptionPlanInline,)
    list_display = ('name', 'description', 'max_user')


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'organisation', 'status', 'subscription_plan',
        'date_subscribed', 'date_expired')
    list_filter = ('organisation',)


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
