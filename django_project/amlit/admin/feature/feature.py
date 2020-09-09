__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '09/09/20'

from django.contrib import admin
from amlit.admin.feature.base import BaseFeatureAdmin
from amlit.models.feature import (
    FeaturePolygon, FeaturePoint, FeatureLine,
    FeaturePolygonProperty, FeaturePointProperty, FeatureLineProperty
)


class FeaturePolygonPropertyInline(admin.TabularInline):
    model = FeaturePolygonProperty


class FeaturePolygonAdmin(BaseFeatureAdmin):
    inlines = [FeaturePolygonPropertyInline]


admin.site.register(FeaturePolygon, FeaturePolygonAdmin)


class FeaturePointPropertyInline(admin.TabularInline):
    model = FeaturePointProperty


class FeaturePointAdmin(BaseFeatureAdmin):
    inlines = [FeaturePointPropertyInline]


admin.site.register(FeaturePoint, FeaturePointAdmin)


class FeatureLinePropertyInline(admin.TabularInline):
    model = FeatureLineProperty


class FeatureLineAdmin(BaseFeatureAdmin):
    inlines = [FeatureLinePropertyInline]


admin.site.register(FeatureLine, FeatureLineAdmin)
