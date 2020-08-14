__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '14/08/20'

from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.redirects.models import Redirect

admin.site.unregister(FlatPage)
admin.site.unregister(Redirect)
