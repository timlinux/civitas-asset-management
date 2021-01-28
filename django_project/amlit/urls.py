__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from django.conf.urls import url, include
from civitas.api import (
    ProjectedReportAPI,
    CommunityAPI, CommunityDetailAPI,
    SummaryAPI, FeaturesGeojsonAPI)
from civitas.view.home import HomeView
from civitas.view.report import ReportPageView

API = [
    # API
    url(r'^report/projected/(?P<year>\d+)$',
        ProjectedReportAPI.as_view(),
        name='civitas-projected-report'),
    url(r'^features/summary$',
        SummaryAPI.as_view(),
        name='civitas-features-summary'),
    url(r'^features/geojson$',
        FeaturesGeojsonAPI.as_view(),
        name='civitas-features-geojson'),

    # community
    url(r'^community/(?P<id>\d+)$',
        CommunityDetailAPI.as_view(),
        name='community-detail'),
    url(r'^community$',
        CommunityAPI.as_view(),
        name='community'),
]

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/', include(API)),
    url(r'^report$', ReportPageView.as_view(), name='civitas-report')
]
