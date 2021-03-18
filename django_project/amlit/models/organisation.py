__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '22/01/21'

from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from amlit.models.user import User
from core.models.term import TermModel


class Organisation(TermModel):
    """
    Organisation that has management.
    Having users with their role.
    Also has the owner
    Organisation can just access specific community
    """

    owner = models.ForeignKey(
        User,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('owner')
    )

    community_code = models.CharField(
        _('community code '),
        max_length=128,
        help_text=_('Community code for this organisation'),
        null=True, blank=True,
    )


class RolePermission(TermModel):
    """
    Permissions for role
    """
    pass


class UserRole(TermModel):
    """
    Role for user in organisation
    """
    permissions = models.ManyToManyField(
        RolePermission,
        verbose_name=_('permissions'),
        blank=True, null=True
    )


class UserOrganisation(models.Model):
    """
    Model that link user with organisation with their role
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('user')
    )
    organisation = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE,
        verbose_name=_('organisation')
    )
    role = models.ForeignKey(
        UserRole,
        on_delete=models.CASCADE,
        verbose_name=_('role')
    )

    class Meta:
        unique_together = ('user', 'organisation')
