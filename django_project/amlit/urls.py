__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from django.conf.urls import url, include
from amlit.api import (
    GetBoxGeojson,
    GetWaterSystem, GetWaterSystems)

WATER_API = [
    # API
    url(r'^system/(?P<id>\d+)',
        GetWaterSystem.as_view(),
        name='api-water-system'),
    url(r'^system',
        GetWaterSystems.as_view(),
        name='api-water-systems'),
    url(r'^box/(?P<id>\d+)',
        GetBoxGeojson.as_view(),
        name='api-box')
]

WATER = [
    url('^api/', include(WATER_API))
]
urlpatterns = [
    url('^water/', include(WATER))
]
