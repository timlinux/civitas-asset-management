__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.models import Site
from django.contrib.redirects.models import Redirect
from django.utils.translation import ugettext_lazy as _
from amlit.models import User, UserTitle

admin.site.unregister(FlatPage)
admin.site.unregister(Redirect)


class AmlitUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'title', 'phone')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'title')


admin.site.register(User, AmlitUserAdmin)
admin.site.register(UserTitle, admin.ModelAdmin)
