__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from django.conf.urls import url, include
from amlit.api import ProjectedReportAPI
from amlit.view.report import ReportPageView

API = [
    # API
    url(r'^report/projected/(?P<year>\d+)$',
        ProjectedReportAPI.as_view(),
        name='amlit-projected-report'),
]

urlpatterns = [
    url(r'^api/', include(API)),
    url(r'^report$', ReportPageView.as_view(), name='amlit-report')
]
