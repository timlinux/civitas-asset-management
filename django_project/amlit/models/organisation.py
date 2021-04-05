__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '22/01/21'

from django.contrib.gis.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from amlit.models.user import User
from core.models.term import TermModel


class OrganisationByUser(models.Manager):
    def admin_role(self, user):
        """ Return organisation that user has admin roles
        :type user: User
        """
        organisations = list(UserOrganisation.objects.filter(
            user=user, role__name='Admin').values_list('organisation_id', flat=True))
        return super().get_queryset().filter(Q(owner=user) | Q(id__in=organisations))

    def all_role(self, user):
        """ Return organisation that user has every roles
        :type user: User
        """
        organisations = list(UserOrganisation.objects.filter(
            user=user).values_list('organisation_id', flat=True))
        return super().get_queryset().filter(Q(owner=user) | Q(id__in=organisations))


class Organisation(TermModel):
    """
    Organisation that has management.
    Having users with their role.
    Also has the owner
    Organisation can just access specific community
    """

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('owner')
    )

    community_code = models.CharField(
        _('community code '),
        max_length=128,
        help_text=_('Community code for this organisation'),
        null=True, blank=True,
    )
    by_user = OrganisationByUser()

    # check current active subscription
    subscription = models.ForeignKey(
        'amlit.Subscription',
        on_delete=models.SET_NULL,
        verbose_name=_('Subscription'),
        null=True, blank=True,
        related_name='organisation_subscription'
    )

    def is_admin(self, user):
        """ Return user is admin role
        :type user: User
        """
        if self.owner == user:
            return True
        try:
            return UserOrganisation.objects.get(user=user, organisation=self).role.name == UserRole.ADMIN
        except UserOrganisation.DoesNotExist:
            return False

    def role(self, user):
        """ Return role of
        :type user: User
        """
        if self.owner == user:
            return UserRole.ADMIN
        try:
            return UserOrganisation.objects.get(user=user, organisation=self).role.name
        except UserOrganisation.DoesNotExist:
            return UserRole.UNKNOWN


class RolePermission(TermModel):
    """
    Permissions for role
    """
    pass


class UserRole(TermModel):
    """
    Role for user in organisation
    """
    ADMIN = 'Admin'
    UNKNOWN = 'Unknown'

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
