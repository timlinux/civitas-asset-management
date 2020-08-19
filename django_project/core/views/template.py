__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '13/09/19'

from django.views.generic import TemplateView


class MapView(TemplateView):
    template_name = 'map.html'
