__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from django.conf.urls import url, include
from amlit.api import (
    ProjectedReportAPI,
    CommunityAPI, CommunityDetailAPI,
    SummaryAPI)
from amlit.view.dashboard import DashboardView
from amlit.view.report import ReportPageView

API = [
    # API
    url(r'^report/projected/(?P<year>\d+)$',
        ProjectedReportAPI.as_view(),
        name='amlit-projected-report'),
    url(r'^feature/summary$',
        SummaryAPI.as_view(),
        name='amlit-feature-summary'),

    # community
    url(r'^community/(?P<id>\d+)$',
        CommunityDetailAPI.as_view(),
        name='community-detail'),
    url(r'^community$',
        CommunityAPI.as_view(),
        name='community'),
]

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='dahboard'),
    url(r'^api/', include(API)),
    url(r'^report$', ReportPageView.as_view(), name='amlit-report')
]
