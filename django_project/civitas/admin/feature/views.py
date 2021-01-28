from django.contrib import admin
from civitas.models.view.feature_calculations import FeatureCalculation


class FeatureCalculationAdmin(admin.ModelAdmin):
    pass


admin.site.register(FeatureCalculation, FeatureCalculationAdmin)
