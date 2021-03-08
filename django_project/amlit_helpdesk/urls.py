__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from django.conf.urls import url
from django.urls import include

from amlit_helpdesk.api.ticket import FeatureTicketListView
from amlit_helpdesk.views import public

app_name = 'amlit_helpdesk'

api_url = [
    url(r'^feature-ticket/(?P<id>\d+)/tickets/$',
        view=FeatureTicketListView.as_view(),
        name='feature-ticket-list'),
]
urlpatterns = [
    url(r'^tickets/submit/$',
        public.create_ticket,
        name='submit'),
    url(r'^api/', include(api_url)),
]
