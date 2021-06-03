__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from django.conf.urls import url, include
from amlit.views.home import HomeView
from amlit.views.report import ReportPageView
from amlit.views.organisations import (
    OrganisationCreateView,
    OrganisationEditView,
    OrganisationListView,
    SubscriptionView,
    SubscriptionCompleteView
)
from civitas.api import (
    ProjectedReportAPI,
    CommunityAPI, CommunityDetailAPI,
    FeatureGeojsonDetailAPI,
    SummaryAPI)

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
    url(r'^create',
        view=OrganisationCreateView.as_view(),
        name='organisation_create'),
    url(r'',
        view=OrganisationListView.as_view(),
        name='organisation_list'),
]

FEATURE_API = [
    url(r'^(?P<pk>\d+)',
        view=FeatureGeojsonDetailAPI.as_view(),
        name='feature-detail'),
]

API = [
    # API
    url(r'^report/projected/(?P<year>\d+)$',
        ProjectedReportAPI.as_view(),
        name='civitas-projected-report'),
    url(r'^feature/', include(FEATURE_API)),
    url(r'^features/summary$',
        SummaryAPI.as_view(),
        name='civitas-features-summary'),

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
