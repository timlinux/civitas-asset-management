__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from django.conf.urls import url, include
from amlit.api import (
    GetSystem, GetSystems, ProjectedReportAPI)
from amlit.view.report import ReportPageView

API = [
    # API
    url(r'^system/(?P<id>\d+)',
        GetSystem.as_view(),
        name='api-system'),
    url(r'^system',
        GetSystems.as_view(),
        name='api-systems'),
]

urlpatterns = [
    url(r'^api/', include(API)),
    url(r'^api/report/projected/(?P<year>\d+)$',
        ProjectedReportAPI.as_view(),
        name='amlit-projected-report'),
    url(r'^report$', ReportPageView.as_view(), name='amlit-report')
]
