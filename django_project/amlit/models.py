__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '22/01/21'

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from phone_field import PhoneField


class UserTitle(models.Model):
    name = models.CharField(_('title'), max_length=150, blank=True)
    description = models.TextField(
        _('description'),
        null=True, blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """

    title = models.ForeignKey(
        UserTitle,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('title')
    )
    phone = PhoneField(
        blank=True, help_text=_('Contact phone number'))
