__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from django.conf.urls import url
from amlit_helpdesk.views import public

app_name = 'amlit_helpdesk'

urlpatterns = [
    url(r'^tickets/submit/$',
        public.create_ticket,
        name='submit'),
]
