__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/03/21'

from django.contrib import admin
from amlit.models import Organisation, UserOrganisation, UserRole, RolePermission
from amlit.forms.organisation import OrganisationForm


class UserOrganisationInline(admin.TabularInline):
    model = UserOrganisation
    extra = 1


class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'community_code')
    inlines = (UserOrganisationInline,)
    form = OrganisationForm


class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    filter_horizontal = ('permissions',)


class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(RolePermission, RolePermissionAdmin)
