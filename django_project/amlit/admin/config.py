__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from amlit.models.config import Configuration
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from django.urls import reverse

csrf_protect_m = method_decorator(csrf_protect)


class ConfigurationAdmin(admin.ModelAdmin):

    @csrf_protect_m
    def changelist_view(self, request, extra_context=None):
        """
        If we only have a single preference object redirect to it,
        otherwise display listing.
        """
        model = self.model
        if model.objects.all().count() > 1:
            return super(ConfigurationAdmin, self).changelist_view(request)
        else:
            obj = model.load()
            return redirect(
                reverse(
                    'admin:%s_%s_change' % (
                        model._meta.app_label, model._meta.model_name
                    ),
                    args=(obj.id,)
                )
            )


admin.site.register(Configuration, ConfigurationAdmin)
