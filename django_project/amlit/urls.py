__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from django.conf.urls import url, include
from amlit.views.home import HomeView
from amlit.views.report import ReportPageView
from amlit.views.organisations import (
    OrganisationEditView,
    OrganisationListView,
    SubscriptionView,
    SubscriptionCompleteView
)
from civitas.api import (
    ProjectedReportAPI,
    CommunityAPI, CommunityDetailAPI,
    SummaryAPI, FeaturesGeojsonAPI)

organisation_url = [
    url(r'^(?P<pk>\d+)/edit',
        view=OrganisationEditView.as_view(),
        name='organisation_edit'),
    url(r'^(?P<pk>\d+)/subscription/complete',
        SubscriptionCompleteView.as_view(),
        name='organisation_subscription_complete'),
    url(r'^(?P<pk>\d+)/subscription',
        SubscriptionView.as_view(),
        name='organisation_subscription'),
    url(r'',
        view=OrganisationListView.as_view(),
        name='organisation_list'),
]

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
    url(r'^report$', ReportPageView.as_view(), name='civitas-report'),
    url(r'^amlit/helpdesk/', include('amlit_helpdesk.urls')),
    url(r'^organisation/', include(organisation_url))
]
